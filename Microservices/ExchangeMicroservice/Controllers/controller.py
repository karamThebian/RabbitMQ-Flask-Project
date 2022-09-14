import json
from Services.get_order_service import get_order
from Services.post_order_service import post_order
from flask import Blueprint,request
controller = Blueprint('controller',__name__)



@controller.route('/Message',methods = ['POST'])
def produceOrder():
    data = json.loads(request.data)
    return post_order(data)
@controller.route('/Consume',methods = ['GET'])
def consumeMessage():
    return get_order()