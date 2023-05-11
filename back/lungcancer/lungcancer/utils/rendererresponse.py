'''
自定义返回处理
'''

# 导入控制返回的JSON格式的类
from rest_framework.renderers import JSONRenderer
from rest_framework import status

class customrenderer(JSONRenderer):
    # 重构render方法
    def render(self, data, accepted_media_type=None, renderer_context=None):
        
        if renderer_context:
            if isinstance(data, dict):
                msg = data.pop('message', 'success')
                code = data.pop('code', status.HTTP_200_OK)
                data = data.pop('data',[])
            else:
                msg = 'success'
                code = status.HTTP_200_OK
                state = 1

            # 重新构建返回的JSON字典
            print(data)
            # for key in data:
                
            #     # 判断是否有自定义的异常的字段
            #     if key == 'message':
            #         msg = data[key]
            #         data = ''
            #         code = code

            ret = {
                'msg': msg,
                'code': code,
                'data': data,
            }
            # 返回JSON数据
            return super().render(ret, accepted_media_type, renderer_context)
        else:
            return super().render(data, accepted_media_type, renderer_context)
