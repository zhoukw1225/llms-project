# 文件说明：
    qwen-agent.py是原作者的运行文件，但是由于千问更新版本，所以更新了调用大模型的方法——llm
    agent.py是新版本的agent——使用app_id和api_key
    agent1.py是旧版本的agent——使用access_key_id和access_key_secret和agent_key和app_id
# 千问相关key和api申请：
    1.在阿里云RAM访问控制台创建新用户【https://ram.console.aliyun.com/users】，创建完成后，再创建AccessKey——————「得到access_key_id和access_key_secret」
    2.给这个用户【https://ram.console.aliyun.com/permissions】添加百炼访问权限AliyunSFMFullAccess或者AliyunSFMReadOnlyAccess
    3.在阿里云百炼平台【https://bailian.console.aliyun.com/】的”我的应用“创建应用「获得agent_key和app_id」
    4.在阿里云百炼平台账号管理给刚刚创建的用户添加的创建好应用的权限

# agent

基于qwen的agent demo，支持历史对话

## 依赖

基于阿里云百炼的通义千问200B大模型