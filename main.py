import logging
import random
import requests  # 导入requests库
from astrbot.api.star import Context, Star, register
from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.event.filter import event_message_type, EventMessageType


logger = logging.getLogger(__name__)

ys_text_list = [
    "你说的对，但是《原神》是由米哈游自主研发的一款全新开放世界冒险游戏。游戏发生在一个被称作「提瓦特」的幻想世界，在这里，被神选中的人将被授予「神之眼」，导引元素之力。你将扮演一位名为「旅行者」的神秘角色，在自由的旅行中邂逅性格各异、能力独特的同伴们，和他们一起击败强敌，找回失散的亲人——同时，逐步发掘「原神」的真相。",
    "原神，启动！",
    "旅行者，我们走！",
    "啊？你在做什么啊？",
    "不要过来啊！",
    # 在这里添加更多从网上找到的“原神圣经”
    "只要抽不死，就往死里抽！",
    "呜呜呜，我的保底没了！",
    "旅行者，你知道吗？派蒙其实是……",
    "今天你充值了吗？",
    "刻晴，我的刻晴！",
    "甘雨，嘿嘿，甘雨……",
    "抽卡一时爽，一直抽卡一直爽！",
    "提瓦特大陆欢迎你！",
    "元素反应，启动！",
    "这合理吗？",
    "策划我***！",
    "米哈游，你没有心！",
    "哎嘿~",
    "旅行者，我们去下一个国家吧！",
    "等我攒够原石，一定把你带回家！",
    "我与提瓦特众生为敌！",
    "旅行者，前方高能！",
    "是风！",
    "旅行者，你知道星尘商店吗？",
    "感谢米哈游，让我体验到这么棒的游戏！",
    "再氪亿点！",
    "我的钱包已经空了……",
    "原神真好玩！",
    "呜呜呜，又歪了……",
    "旅行者，快去完成每日委托吧！",
    "又是美好的一天，从原神开始！"
]

@register("genshinimpact", "ましろSaber", "一个原神启动插件", "1.1", "repo url")
class GenshinImpactPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @event_message_type(EventMessageType.ALL)
    async def on_message(self, event: AstrMessageEvent) -> MessageEventResult:
        """
        当消息中包含“原神”时随机发送一条圣经。
        """
        msg_obj = event.message_obj
        text = msg_obj.message_str or ""

        logger.debug("=== Debug: AstrBotMessage ===")
        logger.debug("Bot ID: %s", msg_obj.self_id)
        logger.debug("Session ID: %s", msg_obj.session_id)
        logger.debug("Message ID: %s", msg_obj.message_id)
        logger.debug("Sender: %s", msg_obj.sender)
        logger.debug("Group ID: %s", msg_obj.group_id)
        logger.debug("Message Chain: %s", msg_obj.message)
        logger.debug("Raw Message: %s", msg_obj.raw_message)
        logger.debug("Timestamp: %s", msg_obj.timestamp)
        logger.debug("============================")

        if "原神" in text:
            # 随机抽取一条圣经
            selected_text = random.choice(ys_text_list)
            yield event.plain_result(selected_text)
