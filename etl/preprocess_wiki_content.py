import sys
import os
project_path = os.path.dirname(os.getcwd())
sys.path.append(project_path)
import datetime
import re
import textile
import pandas as pd
from bs4 import BeautifulSoup
from sqlalchemy import text
from io import StringIO
from config import SQLALCHEMY_DATABASE_URI_2
from webservices.models.models import create_engine_from_uri
from get_feedback_data import GetFeedbackData

feedback_data_obj = GetFeedbackData()



class PrepareModelDataset():
        def __init__(self):
                self.engine = create_engine_from_uri(SQLALCHEMY_DATABASE_URI_2)
                self.include_df = self.data_for_include_section()

        def data_for_include_section(self):
                with self.engine.connect() as connection:
                        include_records_query = """
                                SELECT wp.id, identifier, title, text FROM wiki_pages wp
                                left join wiki_contents on wp.id = wiki_contents.page_id
                                left join wikis on wp.wiki_id = wikis.id
                                left join projects on wikis.project_id = projects.id
                        """

                        include_records = connection.execute(text(include_records_query)).fetchall()
                        include_df = pd.DataFrame(include_records)
                return include_df
        
        def generate_question(self, row):
                questions = [
                        f"識別子が「{row['identifier']}」、モジュールが「{row['module']}」、エージェントが「{row['agent']}」、障害状態が「{row['state']}」の場合、対応手順はどうなるでしょうか？",
                        f"識別子「{row['identifier']}」、モジュール「{row['module']}」、エージェント「{row['agent']}」、障害状態「{row['state']}」の場合に行う対応手順は何ですか?",
                        f"識別子「{row['identifier']}」、モジュール「{row['module']}」、エージェント「{row['agent']}」、および障害状態「{row['state']}」に基づいて発生されたシナリオの場合、標準的な対応手順は何になりますか?",
                        f"識別子が「{row['identifier']}」、モジュールが「{row['module']}」、エージェントが「{row['agent']}」、障害状態が「{row['state']}」の場合、推奨される対応手順は何ですか?"
                ]
                return questions
        
        def df_based_question_format(self, input_df):
                expanded_records = []
                for _, row in input_df.iterrows():
                        questions = self.generate_question(row)
                        for question in questions:
                                record = row.copy()
                                record['question'] = question
                                expanded_records.append(record)
                expanded_df = pd.DataFrame(expanded_records)
                return expanded_df
        
        def get_feedback_collected_data(self):
                df = feedback_data_obj.get_wiki_content()
                distinct_df = df.drop_duplicates(subset=['decoded_correct_url'])
                test_df_other_than_distinct = df.drop(distinct_df.index)
                return distinct_df, test_df_other_than_distinct
    
        # Function to include wiki content in include tag, like {{include(iwakura-op:岩倉ネジ製作所 連絡先)}}
        def add_include_section(self, text, identifier):
                text = text.replace('※', '')
                pattern = r'{{include\((.*?)\)}}'
                while True:
                        matches = re.finditer(pattern, text)
                        match_list = [match for match in matches]
                        if not match_list:
                                break
                        for record in match_list:
                                include_text = record.group(1).split(':')[-1]
                                if not '連絡先' in include_text:
                                        filt_df = self.include_df[(self.include_df['identifier'].str.lower()==identifier.lower()) & (self.include_df['title'].str.lower()==include_text.lower())]
                                        if not filt_df.empty:
                                                include_text_content = filt_df.iloc[0]['text']
                                                text = text.replace(record.group(0), include_text_content)
                                        else:
                                                text = text.replace(record.group(0), '')
                                else:
                                        text = text.replace(record.group(0), '')
                return text

        # Function to get only wiki title text from text like [[iwakura-op:インターネット経由ping疎通]], only if text is under header tag
        def get_wiki_title(self, text):
                pattern_header_with_title = re.compile(r'h[1-6]\.\s*(.*?)\n', re.DOTALL)
                match = re.finditer(pattern_header_with_title, text)
                pattern_after_colon = r':(.*?)\]\]'
                pattern_before_colon = r'\[\[(.*?):'
                pattern_colon_pipe = r':(.*?)\|'
                pattern_text_between_bracket = r'\[\[(.*?)\]\]'
                is_match = [mat for mat in match]
                if is_match:
                        count = 0
                        for match_record in is_match:
                                # get match for pattern colon, on text indexed on start and end text 
                                match_pattern_colon_pipe = re.search(pattern_colon_pipe, match_record.group(0))
                                match_pattern_after_colon = re.search(pattern_after_colon, match_record.group(0))
                                match_pattern_before_colon = re.search(pattern_before_colon, match_record.group(0))
                                match_pattern_between_bracket = re.search(pattern_text_between_bracket, match_record.group(0))
                                if match_pattern_colon_pipe:
                                        extracted_title = match_pattern_colon_pipe.group(1) if count == 0 else match_pattern_colon_pipe.group(1)
                                        text_to_replace = match_record.group(1)
                                        index = text.find(text_to_replace)
                                        text = text[:index] + extracted_title + text[index + len(text_to_replace):]
                                elif match_pattern_after_colon:
                                        extracted_title = match_pattern_after_colon.group(1) if count == 0 else match_pattern_after_colon.group(1)
                                        text_to_replace = match_record.group(1)
                                        index = text.find(text_to_replace)
                                        text = text[:index] + extracted_title + text[index + len(text_to_replace):]
                                elif match_pattern_before_colon:
                                        extracted_title = match_pattern_before_colon.group(1) if count == 0 else match_pattern_before_colon.group(1)
                                        text_to_replace = match_record.group(1)
                                        index = text.find(text_to_replace)
                                        text = text[:index] + extracted_title + text[index + len(text_to_replace):]
                                elif match_pattern_between_bracket:
                                        extracted_title = match_pattern_between_bracket.group(1) if count == 0 else match_pattern_between_bracket.group(1)
                                        text_to_replace = match_record.group(1)
                                        index = text.find(text_to_replace)
                                        text = text[:index] + extracted_title + text[index + len(text_to_replace):]
                                else:
                                        if count == 0:
                                                first_record = match_record.group(0)
                                                match_first_record_heading = re.search(pattern_header_with_title, first_record)
                                                if match_first_record_heading:
                                                        if '概要' not in first_record:
                                                                text_to_replace = match_first_record_heading.group(1)
                                                                extracted_title = match_first_record_heading.group(1)
                                                                index = text.find(text_to_replace)
                                                                text = text[:index] + extracted_title + text[index + len(text_to_replace):]
                                        else:
                                                count = count + 1
                                                continue
                                count = count + 1
                        return text
                else:
                        return text
                
        # Function to remove header html tags like h1, h2 from wiki content
        def remove_header_tags(self, text):
                pattern = re.compile(r'h[1-6]\.\s*', re.DOTALL)
                modified_text = pattern.sub('', text)
                return modified_text

        # Function to replace oredered and unordered list by tab space
        def add_tab(self, text):
                lines = text.split('\n')
                for i, line in enumerate(lines):
                        if line.startswith('**'):
                                match_stars = re.match(r'^\*+', line)
                                num_stars = 0
                                if match_stars:
                                        num_stars = len(match_stars.group(0))
                                lines[i] = '\t'*num_stars + line.lstrip('* ')
                        elif line.startswith('##'):
                                match_stars = re.match(r'^\#+', line)
                                num_stars = 0
                                if match_stars:
                                        num_stars = len(match_stars.group(0))
                                lines[i] = '\t'*num_stars + line.lstrip('# ')
                        elif line.startswith('*'):
                                lines[i] = '\t' + line.lstrip('* ')
                        elif line.startswith('#'):
                                lines[i] = '\t' + line.lstrip('# ')
                tab_added_text = '\n'.join(lines)
                return tab_added_text

        # Function to remove <pre>... </pre> tags from wiki_content
        def remove_pre_tag(self, text):
                pattern = r'<pre>(.*?)</pre>'
                matches = re.finditer(pattern, text, re.DOTALL) # get matches for pre tag
                match_list = [match for match in matches]
                if match_list:
                        for record in match_list:
                                text_inside_pre = record.group(1)
                                pattern_command_master = r'\$(.*?)(?:\n|$)'
                                pattern_command_hash= r'\#(.*?)(?:\n|$)'
                                pattern_command_master_match = re.findall(pattern_command_master, text_inside_pre) # get matches for command starts with $
                                pattern_command_hash_master_match = re.findall(pattern_command_hash, text_inside_pre) # get matches for command starts with $
                                if pattern_command_master_match or pattern_command_hash_master_match:
                                        lines = [rec_line for rec_line in text_inside_pre.split('\n') if rec_line.strip()]
                                        flag_output = False
                                        for i, line in enumerate(lines):
                                                pattern_command_match = re.search(pattern_command_master, line)
                                                hash_match = re.search(pattern_command_hash, line)
                                                if hash_match:
                                                        lines[i] = '次のコマンドを実行します\n' + hash_match[1].strip()
                                                        flag_output = False
                                                elif pattern_command_match:
                                                        lines[i] = '次のコマンドを実行します\n' + pattern_command_match[1].strip()
                                                        flag_output = False
                                                else:
                                                        lines[i] = '出力例\n' + line.strip() if not flag_output else line.strip()
                                                        flag_output = True
                                        replacement_text = '\n'.join(lines)
                                        text = text.replace(record.group(0), replacement_text)
                                else:
                                        lines = record.group(1).split('\n')        
                                        for i, line in enumerate(lines):
                                                lines[i] = line if line.strip() != '' else ''
                                        replacement_text = '\n'.join(lines)
                                        text = text.replace(record.group(0), replacement_text)
                return text

        def remove_warning_section(self, text):
                pattern_warning = r'{{warning(.*?)}}'
                warning_match = re.finditer(pattern_warning, text, re.DOTALL)
                warning_match_list = [match for match in warning_match]

                if warning_match_list:
                        for record in warning_match_list:
                                replacement_text = record.group(1).strip()
                                text = text.replace(record.group(0), '警告:' + replacement_text)
                return text

        def remove_important_section(self, text):
                pattern_important = r'{{important(.*?)}}'
                important_match = re.finditer(pattern_important, text, re.DOTALL)
                important_match_list = [match for match in important_match]

                if important_match_list:
                        for record in important_match_list:
                                replacement_text = record.group(1).strip()
                                text = text.replace(record.group(0), '重要:' + replacement_text)
                return text

        def remove_note_section(self, text):
                pattern_note = r'{{note(.*?)}}'
                note_match = re.finditer(pattern_note, text, re.DOTALL)
                note_match_list = [match for match in note_match]

                if note_match_list:
                        for record in note_match_list:
                                replacement_text = record.group(1).strip()
                                text = text.replace(record.group(0), '注記:' + replacement_text)
                return text

        def remove_collapse_section(self, text):
                pattern_collapse = r'{{collapse(.*?)}}'
                collapse_match = re.finditer(pattern_collapse, text, re.DOTALL)
                collapse_match_list = [match for match in collapse_match]

                if collapse_match_list:
                        for record in collapse_match_list:
                                replacement_text = record.group(1).strip()
                                text = text.replace(record.group(0), replacement_text)
                return text

        # Functions to remove cut_start and cut_end from wiki_content
        def replace_cut_start(self, match):
                return match.group(1)

        def cut_start_text(self, text):
                cut_start_removed_text = re.sub(r'\{\{cut_start\((.*?)\)\}\}', self.replace_cut_start, text)
                cut_end_removed_text = cut_start_removed_text.replace('{{cut_end}}', '')
                # if cut_start is present without any title, then remove that explicitly
                transformed_text = cut_end_removed_text.replace('{{cut_start}}', '')
                return transformed_text

        # Function to convert table structure to sentences
        def process_tables(self, text):
                html_content = textile.textile(text)
                html_content = re.sub(r'(\t+)<table>', r'<table>', html_content)
                html_content = re.sub(r'</table>.*?(\t+)', r'</table>', html_content)
                table_pattern = re.compile(r'<table>.*?</table>', re.DOTALL)
                tables = re.findall(table_pattern, html_content)
                if tables:
                        for table in tables:
                                table = table.replace('\n', '、')
                                soup = BeautifulSoup(table, 'html.parser')
                                df = pd.read_html(StringIO(str(soup)))[0]
                                df = df.dropna(axis=1, how='all')
                                rename_mapping = {col: col.lstrip('._') for col in df.columns if isinstance(col, str)}
                                df = df.rename(columns=rename_mapping)
                                numeric_columns = pd.to_numeric(df.columns, errors='coerce').notna()
                                if any(numeric_columns):
                                        if len(df.columns) > 1:
                                                df['japanese_text'] = df[0] + ':' + df[1]
                                        else:
                                                numbered_column = range(1, len(df) + 1)
                                                df['numbered_column'] = numbered_column
                                                df['japanese_text'] = df['numbered_column'].astype(str) + '. ' + df[0]
                                        japanese_sentence = '\n'.join(df['japanese_text'])
                                else:
                                        if len(df.columns) == 2:
                                                sentence_list = []
                                                for index, row in df.iterrows():
                                                        keys = row.index
                                                        values = row.values
                                                        sentence = f"{index+1}. {keys[0]}{values[0]}と対応する{keys[1]}は {values[1]}です。"
                                                        sentence_list.append(sentence)
                                                japanese_sentence = '\n'.join(sentence_list)
                                        else:
                                                sentence_list = []
                                                for index, row in df.iterrows():
                                                        sentence_parts = [f"{column}は{value}" for column, value in row.items()]
                                                        sentence = f"{index+1}. " + "、".join(sentence_parts)
                                                        sentence_list.append(sentence)
                                                japanese_sentence = '\n'.join(sentence_list)
                                index_table_start = html_content.find('<table>')
                                index_table_end = html_content.find('</table>') + len('</table>')
                                html_content = html_content.replace(html_content[index_table_start:index_table_end], japanese_sentence)
                        soup_obj = BeautifulSoup(html_content, 'html.parser')
                        plain_text = soup_obj.get_text()
                        return plain_text
                else:
                        return text
                
        def process_links(self, text, title):
                pattern_text_in_bracket = r'\[\[(.*?)\]\]'
                match = re.finditer(pattern_text_in_bracket, text, re.DOTALL)
                match_list = [mat for mat in match]
                if match_list:
                        pattern_after_colon = r':(.*?)\]\]'
                        pattern_pipe = r'\[\[(.*?)\|'
                        pattern_colon_pipe = r':(.*?)\|'
                        pattern_text_between_bracket = r'\[\[(.*?)\]\]'
                        for match_record in match_list:
                                match_pattern_colon_pipe = re.search(pattern_colon_pipe, match_record.group(0))
                                match_pattern_after_colon = re.search(pattern_after_colon, match_record.group(0))
                                match_pattern_pipe = re.search(pattern_pipe, match_record.group(0))
                                match_pattern_between_bracket = re.search(pattern_text_between_bracket, match_record.group(0))
                                if match_pattern_colon_pipe:
                                        extracted_title = '参照URL ' + match_pattern_colon_pipe.group(1)
                                        text_to_replace = match_record.group(0)
                                        index = text.find(text_to_replace)
                                        text = text[:index] + extracted_title + text[index + len(text_to_replace):]
                                elif match_pattern_after_colon:
                                        extracted_title = '参照URL ' + match_pattern_after_colon.group(1)
                                        text_to_replace = match_record.group(0)
                                        index = text.find(text_to_replace)
                                        text = text[:index] + extracted_title + text[index + len(text_to_replace):]
                                elif match_pattern_pipe:
                                        extracted_title = '参照URL ' + match_pattern_pipe.group(1)
                                        text_to_replace = match_record.group(0)
                                        index = text.find(text_to_replace)
                                        text = text[:index] + extracted_title + text[index + len(text_to_replace):] 
                                elif match_pattern_between_bracket:
                                        extracted_title = '参照URL ' + match_pattern_between_bracket.group(1)
                                        text_to_replace = match_record.group(0)
                                        index = text.find(text_to_replace)
                                        text = text[:index] + extracted_title + text[index + len(text_to_replace):] 
                return text

        def overview_is(self, text):
                text = text.replace('○ ', '')
                pattern_get_overview = re.compile(r'h\d\.\s*概要(.*?)h\d\.', re.DOTALL)
                pattern_overview_match = pattern_get_overview.search(text)
                
                pattern_get_overview_monitoring = re.compile(r'h\d\.\s*監視概要(.*?)h\d\.', re.DOTALL)
                pattern_overview_monitoring_match = pattern_get_overview_monitoring.search(text)
                
                pattern_html_heads = re.compile(r'h\d\.(.*?)(?=(?:h[1-6]\.|$))', re.DOTALL)
                pattern_html_heads_match = pattern_html_heads.search(text)
                if pattern_overview_match:
                        overview_section = pattern_overview_match.group(1).strip()
                        return overview_section
                elif pattern_overview_monitoring_match:
                        overview_section = pattern_overview_monitoring_match.group(1).strip()
                        return overview_section
                elif pattern_html_heads_match:
                        overview_section = pattern_html_heads_match.group(1).strip()
                        return overview_section
                else:
                        return text

        def correspondence_procedure(self, text):
                text = text.replace('○ ', '')
                pattern_header_with_title = re.compile(r'h[1-6]\.\s*(.*?)\n', re.DOTALL)
                pattern_header_match = re.finditer(pattern_header_with_title, text)
                
                header_list = [mat.group(0).strip() for mat in pattern_header_match]
                pattern_procedure = re.compile(r'h\d\.\s*対応手順(.*?)(?=h\d\.|$)', re.DOTALL)
                pattern_procedure_match = pattern_procedure.search(text)
                
                pattern_procedure_2 = re.compile(r'h\d\.\s*対応(.*?)(?=h\d\.|$)', re.DOTALL)
                pattern_procedure_2_match = pattern_procedure_2.search(text)
                
                pattern_procedure_3 = re.compile(r'h\d\.\s*障害対応手順(.*?)(?=h\d\.|$)', re.DOTALL)
                pattern_procedure_3_match = pattern_procedure_3.search(text)
                
                pattern_procedure_4 = re.compile(r'h\d\.\s*状況確認(.*?)(?=h\d\.|$)', re.DOTALL)
                pattern_procedure_4_match = pattern_procedure_4.search(text)
                
                pattern_procedure_5 = re.compile(r'h\d\.\s*復旧対応(.*?)(?=h\d\.|$)', re.DOTALL)
                pattern_procedure_5_match = pattern_procedure_5.search(text)
                
                pattern_procedure_6 = re.compile(r'h\d\.\s*インターネット経由の監視(.*?)(?=h\d\.|$)', re.DOTALL)
                pattern_procedure_6_match = pattern_procedure_6.search(text)
                
                pattern_recovery = re.compile(r'h\d\.\s*復旧\s*(.*?)(?=(h[1-6])\.|\Z)', re.DOTALL)
                pattern_recovery_match = pattern_recovery.search(text)
                
                recover_match_flag = False
                status_check_flag = False
                if pattern_procedure_match:
                        procedure_section = pattern_procedure_match.group(1).strip()
                        header_text_to_find = pattern_procedure_match.group(0).strip()
                        while True:
                                if procedure_section:
                                        break
                                else:
                                        header_index = header_list.index(header_text_to_find)
                                        next_header_section = header_list[header_index + 1]
                                        next_header_pattern = re.compile(rf'{next_header_section}(.*?)(?=h\d\.|$)', re.DOTALL)
                                        next_header_content = next_header_pattern.search(text)
                                        if next_header_content:
                                                header_text_to_find = next_header_section
                                                procedure_section = next_header_content.group(1).strip()
                elif pattern_procedure_2_match:
                        procedure_section = pattern_procedure_2_match.group(1).strip()
                elif pattern_procedure_3_match:
                        procedure_section = pattern_procedure_3_match.group(1).strip()
                elif pattern_procedure_4_match:
                        procedure_section = pattern_procedure_4_match.group(1).strip()
                        status_check_flag = True
                elif pattern_procedure_5_match:
                        procedure_section = pattern_procedure_5_match.group(1).strip()
                        recover_match_flag = True
                elif pattern_procedure_6_match:
                        procedure_section = pattern_procedure_6_match.group(1).strip()
                else:
                        procedure_section = ''
                if pattern_procedure_4_match and not status_check_flag:
                        status_check_section = pattern_procedure_4_match.group(1).strip()
                        if procedure_section not in status_check_section:
                                procedure_section = status_check_section + '\n' + procedure_section #+ '\n' + ('\n'.join(recovery_section.split('\n')[1:]))
                if pattern_recovery_match and not recover_match_flag:
                        recovery_section = pattern_recovery_match.group(1).strip()
                        procedure_section = procedure_section + '\n' + ('\n'.join(recovery_section.split('\n')[1:]))
                return procedure_section

        def add_x0001(self, text):
                text = text.replace('\n','_x0001_')
                return text
        
        def preprocess_data(self):
                feedback_data_distinct_df, test_df = self.get_feedback_collected_data()

                # apply operations to preprocess wiki content step by step
                feedback_data_distinct_df.loc[:, 'include_section'] = feedback_data_distinct_df.apply(lambda row: self.add_include_section(row['text'], row['identifier']), axis=1)
                feedback_data_distinct_df.loc[:, 'title_extraction_from_header'] = feedback_data_distinct_df.apply(lambda row: self.get_wiki_title(row['include_section']), axis=1)
                feedback_data_distinct_df.loc[:, 'pre_removed'] = feedback_data_distinct_df.apply(lambda row: self.remove_pre_tag(row['title_extraction_from_header']), axis=1)
                feedback_data_distinct_df.loc[:, 'added_tab'] = feedback_data_distinct_df.apply(lambda row: self.add_tab(row['pre_removed']), axis=1)
                feedback_data_distinct_df.loc[:, 'warning_text'] = feedback_data_distinct_df.apply(lambda row: self.remove_warning_section(row['added_tab']), axis=1)
                feedback_data_distinct_df.loc[:, 'important_text'] = feedback_data_distinct_df.apply(lambda row: self.remove_important_section(row['warning_text']), axis=1)
                feedback_data_distinct_df.loc[:, 'note_text'] = feedback_data_distinct_df.apply(lambda row: self.remove_note_section(row['important_text']), axis=1)
                feedback_data_distinct_df.loc[:, 'collapse'] = feedback_data_distinct_df.apply(lambda row: self.remove_collapse_section(row['note_text']), axis=1)
                feedback_data_distinct_df.loc[:, 'cut_start_removed'] = feedback_data_distinct_df.apply(lambda row: self.cut_start_text(row['collapse']), axis=1)
                feedback_data_distinct_df.loc[:, 'processed_content'] = feedback_data_distinct_df.apply(lambda row: self.process_links(row['cut_start_removed'], row['title']), axis=1)
                feedback_data_distinct_df.loc[:, 'final_processed_content_x0001'] = feedback_data_distinct_df.apply(lambda row: self.add_x0001(row['processed_content']), axis=1)
                print(feedback_data_distinct_df)

                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                file_save_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'webservices/static')

                train_df = self.df_based_question_format(feedback_data_distinct_df)
                train_df.to_excel(f'{file_save_path}/train_data_{timestamp}.xlsx')

                test_data_df = self.df_based_question_format(test_df)
                test_data_df.to_excel(f'{file_save_path}/test_data_{timestamp}.xlsx')
                return train_df

# obj = PrepareModelDataset()
# obj.preprocess_data()
# leaf_records_df2 = leaf_records_df.copy()

# leaf_records_df2.loc[:, 'include_section'] = leaf_records_df2.apply(lambda row: add_include_section(row['text'], row['identifier']), axis=1)
# leaf_records_df2.loc[:, 'title_extraction_from_header'] = leaf_records_df2.apply(lambda row: get_wiki_title(row['include_section']), axis=1)
# leaf_records_df2.loc[:, 'pre_removed'] = leaf_records_df2.apply(lambda row: remove_pre_tag(row['title_extraction_from_header']), axis=1)
# leaf_records_df2.loc[:, 'added_tab'] = leaf_records_df2.apply(lambda row: add_tab(row['pre_removed']), axis=1)
# leaf_records_df2.loc[:, 'warning_text'] = leaf_records_df2.apply(lambda row: remove_warning_section(row['added_tab']), axis=1)
# leaf_records_df2.loc[:, 'important_text'] = leaf_records_df2.apply(lambda row: remove_important_section(row['warning_text']), axis=1)
# leaf_records_df2.loc[:, 'note_text'] = leaf_records_df2.apply(lambda row: remove_note_section(row['important_text']), axis=1)
# leaf_records_df2.loc[:, 'collapse'] = leaf_records_df2.apply(lambda row: remove_collapse_section(row['note_text']), axis=1)
# leaf_records_df2.loc[:, 'cut_start_removed'] = leaf_records_df2.apply(lambda row: cut_start_text(row['collapse']), axis=1)
# leaf_records_df2.loc[:, 'processed_content'] = leaf_records_df2.apply(lambda row: process_links(row['cut_start_removed'], row['title']), axis=1)
# leaf_records_df2.loc[:, 'final_processed_content_x0001'] = leaf_records_df2.apply(lambda row: add_x0001(row['processed_content']), axis=1)

# # to get overview content
# leaf_records_df2.loc[:, 'overview_content'] = leaf_records_df2.apply(lambda row: overview_is(row['text']), axis=1)
# leaf_records_df2.loc[:, 'include_section_for_overview'] = leaf_records_df2.apply(lambda row: add_include_section(row['overview_content'], row['identifier']), axis=1)
# leaf_records_df2.loc[:, 'title_extraction_from_header_for_overview'] = leaf_records_df2.apply(lambda row: get_wiki_title(row['include_section_for_overview']), axis=1)
# leaf_records_df2.loc[:, 'header_removed_for_overview'] = leaf_records_df2.apply(lambda row: remove_header_tags(row['title_extraction_from_header_for_overview']), axis=1)
# leaf_records_df2.loc[:, 'pre_removed_for_overview'] = leaf_records_df2.apply(lambda row: remove_pre_tag(row['header_removed_for_overview']), axis=1)
# leaf_records_df2.loc[:, 'added_tab_for_overview'] = leaf_records_df2.apply(lambda row: add_tab(row['pre_removed_for_overview']), axis=1)
# leaf_records_df2.loc[:, 'warning_text_for_overview'] = leaf_records_df2.apply(lambda row: remove_warning_section(row['added_tab_for_overview']), axis=1)
# leaf_records_df2.loc[:, 'important_text_for_overview'] = leaf_records_df2.apply(lambda row: remove_important_section(row['warning_text_for_overview']), axis=1)
# leaf_records_df2.loc[:, 'note_text_for_overview'] = leaf_records_df2.apply(lambda row: remove_note_section(row['important_text_for_overview']), axis=1)
# leaf_records_df2.loc[:, 'collapse_text_for_overview'] = leaf_records_df2.apply(lambda row: remove_collapse_section(row['note_text_for_overview']), axis=1)
# leaf_records_df2.loc[:, 'cut_start_removed_for_overview'] = leaf_records_df2.apply(lambda row: cut_start_text(row['collapse_text_for_overview']), axis=1)
# leaf_records_df2.loc[:, 'final_overview_content'] = leaf_records_df2.apply(lambda row: process_links(row['cut_start_removed_for_overview'], row['title']), axis=1)

# # to get correspondence procedure section
# leaf_records_df2.loc[:, 'correspondence_procedure'] = leaf_records_df2.apply(lambda row: correspondence_procedure(row['text']), axis=1)
# leaf_records_df2.loc[:, 'include_section_for_procedure'] = leaf_records_df2.apply(lambda row: add_include_section(row['correspondence_procedure'], row['identifier']), axis=1)
# leaf_records_df2.loc[:, 'title_extraction_from_header_for_procedure'] = leaf_records_df2.apply(lambda row: get_wiki_title(row['include_section_for_procedure']), axis=1)
# leaf_records_df2.loc[:, 'header_removed_for_procedure'] = leaf_records_df2.apply(lambda row: remove_header_tags(row['title_extraction_from_header_for_procedure']), axis=1)
# leaf_records_df2.loc[:, 'pre_removed_for_procedure'] = leaf_records_df2.apply(lambda row: remove_pre_tag(row['header_removed_for_procedure']), axis=1)
# leaf_records_df2.loc[:, 'added_tab_for_procedure'] = leaf_records_df2.apply(lambda row: add_tab(row['pre_removed_for_procedure']), axis=1)
# leaf_records_df2.loc[:, 'warning_text_for_procedure'] = leaf_records_df2.apply(lambda row: remove_warning_section(row['added_tab_for_procedure']), axis=1)
# leaf_records_df2.loc[:, 'important_text_for_procedure'] = leaf_records_df2.apply(lambda row: remove_important_section(row['warning_text_for_procedure']), axis=1)
# leaf_records_df2.loc[:, 'note_text_for_procedure'] = leaf_records_df2.apply(lambda row: remove_note_section(row['important_text_for_procedure']), axis=1)
# leaf_records_df2.loc[:, 'collapse_text_for_procedure'] = leaf_records_df2.apply(lambda row: remove_collapse_section(row['note_text_for_procedure']), axis=1)
# leaf_records_df2.loc[:, 'cut_start_removed_for_procedure'] = leaf_records_df2.apply(lambda row: cut_start_text(row['collapse_text_for_procedure']), axis=1)
# leaf_records_df2.loc[:, 'final_correspondence_procedure'] = leaf_records_df2.apply(lambda row: process_links(row['cut_start_removed_for_procedure'], row['title']), axis=1)

# expanded_records = []

# # Iterate over each row in the original DataFrame
# for _, row in leaf_records_df2.iterrows():
#         questions = generate_question(row)
#         # Create four records with different questions
#         for question in questions:
#                 record = row.copy()
#                 record['question'] = question
#                 expanded_records.append(record)

# # Convert the expanded records to a new DataFrame
# expanded_df = pd.DataFrame(expanded_records)


# selected_columns = ['module', 'state', 'agent', 'mod_state_agent_id', 'prepared_query', 'correct_sop', 'sop_type', 'decoded_correct_url', 'title', 'identifier','text', 'processed_content', 'final_overview_content', 'final_correspondence_procedure','question', 'final_processed_content_x0001']
# expanded_df[selected_columns].to_excel('/mnt/data1/imai_phase3_genAI_api/webservices/static/preprocessed_content.xlsx')
