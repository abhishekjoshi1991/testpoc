import re
def remove_pre_tag(text):
        pattern = r'<pre>(.*?)</pre>'
        matches = re.finditer(pattern, text, re.DOTALL) # get matches for pre tag
        match_list = [match for match in matches]
        import pdb; pdb.set_trace()
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
                                replacement_text = 'start of tag' + '\n'.join(lines) + 'end of pre tag\n'
                                text = text.replace(record.group(0), replacement_text)
                        else:
                                lines = record.group(1).split('\n')        
                                for i, line in enumerate(lines):
                                        lines[i] = line if line.strip() != '' else ''
                                replacement_text = '\n'.join(lines)
                                text = text.replace(record.group(0), replacement_text)
        return text

text = """
"h1. nginxサービスの状態 

{{include(ログイン方法)}}

h3. 障害対応手順

サービスの稼働状況を確認し、nginx, php-fpmの再起動を行ってください。

# チケットにて、第一報の連絡を行います。
# nginx, php-fpmサービスの稼働状況を確認します。
* nginx.service
<pre>
sh-4.2$ systemctl status nginx
● nginx.service - The nginx HTTP and reverse proxy server
   Loaded: loaded (/usr/lib/systemd/system/nginx.service; enabled; vendor preset: disabled)
   Active: active (running) since Fri 2022-12-02 19:35:10 JST; 3 months 11 days ago
 Main PID: 14010 (nginx)
   CGroup: /system.slice/nginx.service
           ├─14010 nginx: master process /usr/sbin/nginx
           ├─14011 nginx: worker process
           └─14012 nginx: worker process

Warning: Journal has been rotated since unit was started. Log output is incomplete or unavailable.
sh-4.2$
</pre>
* php-fpm.service
<pre>
sh-4.2$ systemctl status php81-php-fpm.service
● php81-php-fpm.service - The PHP FastCGI Process Manager
   Loaded: loaded (/usr/lib/systemd/system/php81-php-fpm.service; enabled; vendor preset: disabled)
   Active: active (running) since Wed 2023-02-22 15:53:32 JST; 3 weeks 0 days ago
 Main PID: 27816 (php-fpm)
   Status: ""Processes active: 0, idle: 35, Requests: 135828, slow: 0, Traffic: 0.1req/sec"" 
   CGroup: /system.slice/php81-php-fpm.service
           ├─27816 php-fpm: master process (/etc/opt/remi/php81/php-fpm.conf)
           ├─30512 php-fpm: pool www
           ├─30513 php-fpm: pool www
           ├─30514 php-fpm: pool www
           ├─30515 php-fpm: pool www
           ├─31167 php-fpm: pool www
</pre>

# nginx, php-fpmサービスを再起動します。
<pre>
$ sudo systemctl restart nginx.service
$ sudo systemctl restart php81-php-fpm.service
</pre>
# 起動できない場合は、ログなどから原因調査を行ってください。


"""
print(remove_pre_tag(text))