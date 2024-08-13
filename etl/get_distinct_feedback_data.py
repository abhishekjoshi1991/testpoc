# import pandas as pd
# df = pd.read_excel('/mnt/data1/imai_phase3_genAI_api/webservices/static/preprocessed_feedback_data.xlsx')
# selected_columns = ['module', 'state', 'agent', 'mod_state_agent_id',
#        'prepared_query', 'correct_sop', 'sop_type', 'decoded_correct_url',
#        'title', 'identifier', 'text', 'processed_content',
#        'final_processed_content_x0001']
# df_781 = df[selected_columns].copy()

# # save distinct records from feedback data
# distinct_df = df_781.drop_duplicates(subset=['decoded_correct_url'])
# distinct_df.to_excel('/mnt/data1/imai_phase3_genAI_api/webservices/static/distinct_records.xlsx')

# # records other than distinct
# test_data_df_other_than_distinct = df_781.drop(distinct_df.index)
# test_data_df_other_than_distinct.to_excel('/mnt/data1/imai_phase3_genAI_api/webservices/static/records_other_than_distinct.xlsx')

# def generate_question(row):
#     questions = [
#         f"識別子が「{row['identifier']}」、モジュールが「{row['module']}」、エージェントが「{row['agent']}」、障害状態が「{row['state']}」の場合、対応手順はどうなるでしょうか？",
#         f"識別子「{row['identifier']}」、モジュール「{row['module']}」、エージェント「{row['agent']}」、障害状態「{row['state']}」の場合に行う対応手順は何ですか?",
#         f"識別子「{row['identifier']}」、モジュール「{row['module']}」、エージェント「{row['agent']}」、および障害状態「{row['state']}」に基づいて発生されたシナリオの場合、標準的な対応手順は何になりますか?",
#         f"識別子が「{row['identifier']}」、モジュールが「{row['module']}」、エージェントが「{row['agent']}」、障害状態が「{row['state']}」の場合、推奨される対応手順は何ですか?"
#     ]
#     return questions

# expanded_records = []
# for _, row in distinct_df.iterrows():
#         questions = generate_question(row)
#         for question in questions:
#                 record = row.copy()
#                 record['question'] = question
#                 expanded_records.append(record)
                
# expanded_df = pd.DataFrame(expanded_records)
# expanded_df.rename(columns={'final_processed_content_x0001': 'answer'}, inplace=True)

# #save distinct records based on 4 questions
# expanded_df[['question', 'answer']].to_excel('/mnt/data1/imai_phase3_genAI_api/webservices/static/distinct_based_4_questions.xlsx')

# expanded_records_other_than_distinct = []
# for _, row in test_data_df_other_than_distinct.iterrows():
#         # Generate questions for the current row
#         questions = generate_question(row)
#         # Create four records with different questions
#         for question in questions:
#                 record = row.copy()
#                 record['question'] = question
#                 expanded_records_other_than_distinct.append(record)
                
# expanded_df_other_than_testing = pd.DataFrame(expanded_records_other_than_distinct)
# expanded_df_other_than_testing.to_excel('/mnt/data1/imai_phase3_genAI_api/webservices/static/record_other_than_distinct_based_4_questions.xlsx')

import pandas as pd
from get_feedback_data import get_wiki_content

# new code, to get distinct records from feedback data out of all collected records
class PrepareData:
    def get_distinct(self):
        import pdb; pdb.set_trace()
        df = get_wiki_content()
        distinct_df = df.drop_duplicates(subset=['decoded_correct_url'])
        test_df_other_than_distinct = df.drop(distinct_df.index)
        train_df = self.df_based_question_format(distinct_df)
        test_df = self.df_based_question_format(test_df_other_than_distinct)
        return train_df, test_df
    
    # def get_train_test_dataset(self, distinct_df, ):
    #     train_df = self.df_based_question_format(distinct_df)
    #     test_df = self.df_based_question_format(test_df_other_than_distinct)
    
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


        
obj=PrepareData()
obj.get_distinct()