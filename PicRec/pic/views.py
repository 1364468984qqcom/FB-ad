import json
import redis

from tools.new_picture_rec import search_image, del_pic, search_pic, add_to_banlist, del_from_banlist, \
    view_banlist, \
    query_all_duplicate, query_dup, query_dup_gt_num, cal_imagehash, cal_imagehashs

# from tools.picture_rec import search_image, del_pic, search_pic, add_to_banlist, del_from_banlist, view_banlist
# from tools.new_picture_rec import search_image, del_pic, search_pic, add_to_banlist, del_from_banlist, view_banlist, \
#     query_dup_gt_num, query_dup, query_all_duplicate, cal_imagehash, cal_imagehashs
from pic.models import Pic, Pic1
from pic.serializers import PicSerializer, Pic1Serializer, Pic2Serializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

with open('./dja/db.json') as f:
    redis_key = json.loads(f.read())['REDIS_KEY']
    # redis_key = json.loads(f.read())['REDIS_KEY_LOCAL']  # 如需连接本地redis 则将注释去掉

# 数据若储存本地文件，要改成自己的redis接口
pool = redis.ConnectionPool(host=redis_key['host'], port=redis_key['port'], password=redis_key['password'],
                            decode_responses=redis_key['decode_responses'], db=redis_key['db'])

Reds = redis.Redis(connection_pool=pool)


# 图片查重主接口
class PicList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        pics = Pic.objects.all()
        serializer = PicSerializer(pics, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        data1 = search_image(request.data)
        data = request.data
        request.POST._mutable = True
        data['images'] = json.dumps(data['images'])
        request.POST._mutable = False
        serializer = PicSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        serializer1 = Pic1Serializer(data=data1)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data, status=status.HTTP_201_CREATED)
        return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)


# 商品详情获取
class PicDetail(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Pic.objects.get(pk=pk)
        except Pic.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pic = self.get_object(pk)
        serializer = PicSerializer(pic)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pic = self.get_object(pk)
        serializer = PicSerializer(pic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pic = self.get_object(pk)
        p = Pic1.objects.get(pid=pk)
        pic.delete()
        p.delete()
        pid = Reds.hget('reverse', pk)
        Reds.hdel('imagehash', pid)
        Reds.hdel('reverse', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


# 图片删除
class PicDel(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = dict(request.data)
        data = del_pic(data['images'])
        return Response(data, status=status.HTTP_202_ACCEPTED)


# 以图搜图
class PicSearch(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        urls = request.data['images']
        data = search_pic(urls)
        return Response(data, status=status.HTTP_202_ACCEPTED)


# 查看黑名单
class ViewBanList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = view_banlist()
        return Response(data, status=status.HTTP_200_OK)


# 加入黑名单
class AddToBanList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = dict(request.data)
        data = add_to_banlist(data['images'])
        return Response(data, status=status.HTTP_202_ACCEPTED)


# 从黑名单删除
class RemFromBanList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = dict(request.data)
        data = del_from_banlist(data['images'])
        return Response(data, status=status.HTTP_202_ACCEPTED)


# 黑名单功能,图片筛选
# 此接口查询哪些商品有正整数个商品与之重复,返回图片的哈希值为key,商品ID列表为value的字典
class QueryDupGtNum(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):  # pk为主键
        pk = pk or 10  # 如果pk为True，则为pk=pk。如果pk为False，则为pk=10
        data = query_dup_gt_num(pk)
        return Response(data, status=status.HTTP_202_ACCEPTED)

    def post(self, request, format=None, pk=10):
        data = query_dup(request.data)
        return Response(data, status=status.HTTP_200_OK)


class QueryDupAll(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = query_all_duplicate()
        return Response(data, status=status.HTTP_202_ACCEPTED)


# 此接口为图片哈希值计算接口，传入单个图片链接，返回图片的商品的哈希值
class CalImageHash(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        urls = request.data['images']
        data = cal_imagehash(urls)
        return Response(data, status=status.HTTP_202_ACCEPTED)


# 此接口为图片哈希值计算接口，传入多个图片链接，返回多个图片的商品的哈希值
class CalImageHashs(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = dict(request.data)
        urls = data['images']
        data = cal_imagehashs(urls)
        return Response(data, status=status.HTTP_202_ACCEPTED)
