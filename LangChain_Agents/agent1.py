import os
import broadscope_bailian

# https://help.aliyun.com/zh/model-studio/videos/python-sdk-previous-version?spm=5176.2020520104.0.0.276c3f1bmKGOuf#fc7d3f0074p0s
def test_completions():
    access_key_id = ""
    access_key_secret = ""
    agent_key = ""
    app_id = ""

    client = broadscope_bailian.AccessTokenClient(access_key_id=access_key_id, access_key_secret=access_key_secret,
                                                  agent_key=agent_key)
    token = client.get_token()

    prompt = "帮我生成一篇200字的文章，描述一下春秋战国的政治、军事和经济"
    resp = broadscope_bailian.Completions(token=token).call(app_id=app_id, prompt=prompt)

    if not resp.get("Success"):
        print('failed to create completion, request_id: %s, code: %s, message: %s' % (
            resp.get("RequestId"), resp.get("Code"), resp.get("Message")))
        return

    print("request_id: %s, text: %s" % (resp.get("RequestId"), resp.get("Data", "").get("Text")))
    if resp.get("Data", "").get("Usage") is not None and len(resp.get("Data", "").get("Usage")) > 0:
        usage = resp.get("Data", "").get("Usage")[0]
        print("input tokens: %d, output tokens: %d" % (usage.get("InputTokens"), usage.get("OutputTokens")))


test_completions()