# -*- coding: utf-8 -*-

# @Author  : wzdnzd
# @Time    : 2022-11-12

import json

import push
from logger import logger


<<<<<<< HEAD
def persist(engine: str, data: dict, persist: dict, meta: str = "") -> None:
    try:
        pushtool = push.get_instance(engine=engine)
        if data is None or type(data) != dict or not pushtool.validate(push_conf=persist):
            logger.debug(f"[{meta}] skip persist subscibes because fileid or data is empty")
            return

        pushtool.push_to(content=json.dumps(data), push_conf=persist, group="subscribes")
=======
def persist(config: push.PushConfig, data: dict, persist: dict, meta: str = "") -> None:
    try:
        pushtool = push.get_instance(config=config)
        if data is None or type(data) != dict or not pushtool.validate(config=persist):
            logger.debug(f"[{meta}] skip persist subscibes because fileid or data is empty")
            return

        pushtool.push_to(content=json.dumps(data), config=persist, group="subscribes")
>>>>>>> a3c13dff82e3a5c487b3d8fd829857fd50f6c7c2
    except:
        logger.error(f"[{meta}] occur error when persist subscribes")
