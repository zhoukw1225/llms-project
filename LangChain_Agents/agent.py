import os
from http import HTTPStatus
from dashscope import Application

# https://help.aliyun.com/zh/model-studio/developer-reference/call-alibaba-cloud-model-studio-through-sdk?spm=a2c4g.11186623.0.0.4c6a34462ois7g
def call_agent_app():
    response = Application.call(app_id=os.environ.get("APP_ID"),
                                prompt='如何做炒西红柿鸡蛋？',
                                api_key=os.environ.get("API_KEY"),
                                )

    if response.status_code != HTTPStatus.OK:
        print('request_id=%s, code=%s, message=%s\n' % (response.request_id, response.status_code, response.message))
    else:
        print('request_id=%s\n output=%s\n usage=%s\n' % (response.request_id, response.output, response.usage))


def call_with_session():
    response = Application.call(app_id=os.environ.get("APP_ID"),
                                prompt='我想去新疆',
                                api_key=os.environ.get("API_KEY"),
                                )

    if response.status_code != HTTPStatus.OK:
        print('request_id=%s, code=%s, message=%s\n' % (response.request_id, response.status_code, response.message))
        return

    response = Application.call(app_id=os.environ.get("APP_ID"),
                                prompt='那边有什么旅游景点或者美食?',
                                session_id=response.output.session_id,
                                api_key=os.environ.get("API_KEY"),
                                )
    if response.status_code != HTTPStatus.OK:
        print('request_id=%s, code=%s, message=%s\n' % (response.request_id, response.status_code, response.message))
    else:
        print('request_id=%s, output=%s, usage=%s\n' % (response.request_id, response.output, response.usage))


if __name__ == '__main__':
    call_agent_app()
    call_with_session()
