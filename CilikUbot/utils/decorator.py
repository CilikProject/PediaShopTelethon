

import inspect
import re
from pathlib import Path

from telethon import events

from CilikUbot import (
    BL_CHAT,
    CMD_HANDLER,
    CMD_LIST,
    LOAD_PLUG,
    CILIK2,
    CILIK3,
    CILIK4,
    CILIK5,
    CILIK6,
    CILIK7,
    CILIK8,
    CILIK9,
    CILIK10,
    CILIK11,
    CILIK12,
    CILIK13,
    CILIK14,
    CILIK15,
    CILIK16,
    CILIK17,
    CILIK18,
    CILIK19,
    CILIK20,
    SUDO_HANDLER,
    SUDO_USERS,
    bot,
    tgbot,
)


def cilik_cmd(
    pattern: str = None,
    allow_sudo: bool = True,
    disable_edited: bool = False,
    forword=False,
    command: str = None,
    **args,
):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    if "disable_edited" in args:
        del args["disable_edited"]

    args["blacklist_chats"] = True
    black_list_chats = list(BL_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    if pattern is not None:
        global cilik_reg
        global sudo_reg
        if (
            pattern.startswith(r"\#")
            or not pattern.startswith(r"\#")
            and pattern.startswith(r"^")
        ):
            cilik_reg = sudo_reg = re.compile(pattern)
        else:
            cilik_ = "\\" + CMD_HANDLER
            sudo_ = "\\" + SUDO_HANDLER
            cilik_reg = re.compile(cilik_ + pattern)
            sudo_reg = re.compile(sudo_ + pattern)
            if command is not None:
                cmd1 = cilik_ + command
                cmd2 = sudo_ + command
            else:
                cmd1 = (
                    (cilik_ +
                     pattern).replace(
                        "$",
                        "").replace(
                        "\\",
                        "").replace(
                        "^",
                        ""))
                cmd2 = (
                    (sudo_ + pattern)
                    .replace("$", "")
                    .replace("\\", "")
                    .replace("^", "")
                )
            try:
                CMD_LIST[file_test].append(cmd1)
            except BaseException:
                CMD_LIST.update({file_test: [cmd1]})

    def decorator(func):
        if bot:
            if not disable_edited:
                bot.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=cilik_reg))
            bot.add_event_handler(func, events.NewMessage(
                **args, outgoing=True, pattern=cilik_reg))
        if bot:
            if allow_sudo:
                if not disable_edited:
                    bot.add_event_handler(
                        func,
                        events.MessageEdited(
                            **args,
                            from_users=list(SUDO_USERS),
                            pattern=sudo_reg),
                    )
                bot.add_event_handler(
                    func,
                    events.NewMessage(
                        **args, from_users=list(SUDO_USERS), pattern=sudo_reg
                    ),
                )
        if CILIK2:
            if not disable_edited:
                CILIK2.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=cilik_reg))
            CILIK2.add_event_handler(
                func, events.NewMessage(
                    **args, outgoing=True, pattern=cilik_reg))
        if CILIK3:
            if not disable_edited:
                CILIK3.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=cilik_reg))
            CILIK3.add_event_handler(
                func, events.NewMessage(
                    **args, outgoing=True, pattern=cilik_reg))
        if CILIK4:
            if not disable_edited:
                CILIK4.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=cilik_reg))
            CILIK4.add_event_handler(
                func, events.NewMessage(
                    **args, outgoing=True, pattern=cilik_reg))
        if CILIK5:
            if not disable_edited:
                CILIK5.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=cilik_reg))
            CILIK5.add_event_handler(
                func, events.NewMessage(
                    **args, outgoing=True, pattern=cilik_reg))
        if CILIK6:
            if not disable_edited:
                CILIK6.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=cilik_reg))
            CILIK6.add_event_handler(
                func, events.NewMessage(
                    **args, outgoing=True, pattern=cilik_reg))
        if CILIK7:
            if not disable_edited:
                CILIK7.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=cilik_reg))
            CILIK7.add_event_handler(
                func, events.NewMessage(
                    **args, outgoing=True, pattern=cilik_reg))
        if CILIK8:
            if not disable_edited:
                CILIK8.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=cilik_reg))
            CILIK8.add_event_handler(
                func, events.NewMessage(
                    **args, outgoing=True, pattern=cilik_reg))
        if CILIK9:
            if not disable_edited:
                CILIK9.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=cilik_reg))
            CILIK9.add_event_handler(
                func, events.NewMessage(
                    **args, outgoing=True, pattern=cilik_reg))
        if CILIK10:
            if not disable_edited:
                CILIK10.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=cilik_reg))
            CILIK10.add_event_handler(
                func, events.NewMessage(
                    **args, outgoing=True, pattern=cilik_reg))
        if CILIK11:
            if not disable_edited:
                CILIK11.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=cilik_reg))
            CILIK11.add_event_handler(
                func, events.NewMessage(
                    **args, outgoing=True, pattern=cilik_reg))
        if CILIK12:
            if not disable_edited:
                CILIK12.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=cilik_reg))
            CILIK12.add_event_handler(
                func, events.NewMessage(
                    **args, outgoing=True, pattern=cilik_reg))
        if CILIK13:
            if not disable_edited:
                CILIK13.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=cilik_reg))
            CILIK13.add_event_handler(
                func, events.NewMessage(
                    **args, outgoing=True, pattern=cilik_reg))
        if CILIK14:
            if not disable_edited:
                CILIK14.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=cilik_reg))
            CILIK14.add_event_handler(
                func, events.NewMessage(
                    **args, outgoing=True, pattern=cilik_reg))
        if CILIK15:
            if not disable_edited:
                CILIK15.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=cilik_reg))
            CILIK15.add_event_handler(
                func, events.NewMessage(
                    **args, outgoing=True, pattern=cilik_reg))
        if CILIK16:
            if not disable_edited:
                CILIK16.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=cilik_reg))
            CILIK16.add_event_handler(
                func, events.NewMessage(
                    **args, outgoing=True, pattern=cilik_reg))
        if CILIK17:
            if not disable_edited:
                CILIK17.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=cilik_reg))
            CILIK17.add_event_handler(
                func, events.NewMessage(
                    **args, outgoing=True, pattern=cilik_reg))
        if CILIK18:
            if not disable_edited:
                CILIK18.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=cilik_reg))
            CILIK18.add_event_handler(
                func, events.NewMessage(
                    **args, outgoing=True, pattern=cilik_reg))
        if CILIK19:
            if not disable_edited:
                CILIK19.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=cilik_reg))
            CILIK19.add_event_handler(
                func, events.NewMessage(
                    **args, outgoing=True, pattern=cilik_reg))
        if CILIK20:
            if not disable_edited:
                CILIK20.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=cilik_reg))
            CILIK20.add_event_handler(
                func, events.NewMessage(
                    **args, outgoing=True, pattern=cilik_reg))
        try:
            LOAD_PLUG[file_test].append(func)
        except Exception:
            LOAD_PLUG.update({file_test: [func]})
        return func

    return decorator


def cilik_handler(
    **args,
):
    def decorator(func):
        if bot:
            bot.add_event_handler(func, events.NewMessage(**args))
        if CILIK2:
            CILIK2.add_event_handler(func, events.NewMessage(**args))
        if CILIK3:
            CILIK3.add_event_handler(func, events.NewMessage(**args))
        if CILIK4:
            CILIK4.add_event_handler(func, events.NewMessage(**args))
        if CILIK5:
            CILIK5.add_event_handler(func, events.NewMessage(**args))
        if CILIK6:
            CILIK6.add_event_handler(func, events.NewMessage(**args))
        if CILIK7:
            CILIK7.add_event_handler(func, events.NewMessage(**args))
        if CILIK8:
            CILIK8.add_event_handler(func, events.NewMessage(**args))
        if CILIK9:
            CILIK9.add_event_handler(func, events.NewMessage(**args))
        if CILIK10:
            CILIK10.add_event_handler(func, events.NewMessage(**args))
        if CILIK11:
            CILIK11.add_event_handler(func, events.NewMessage(**args))
        if CILIK12:
            CILIK12.add_event_handler(func, events.NewMessage(**args))
        if CILIK13:
            CILIK13.add_event_handler(func, events.NewMessage(**args))
        if CILIK14:
            CILIK14.add_event_handler(func, events.NewMessage(**args))
        if CILIK15:
            CILIK15.add_event_handler(func, events.NewMessage(**args))
        if CILIK16:
            CILIK16.add_event_handler(func, events.NewMessage(**args))
        if CILIK17:
            CILIK17.add_event_handler(func, events.NewMessage(**args))
        if CILIK18:
            CILIK18.add_event_handler(func, events.NewMessage(**args))
        if CILIK19:
            CILIK19.add_event_handler(func, events.NewMessage(**args))
        if CILIK20:
            CILIK20.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator


def asst_cmd(**args):
    pattern = args.get("pattern", None)
    r_pattern = r"^[/!]"
    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern
    args["pattern"] = pattern.replace("^/", r_pattern, 1)

    def decorator(func):
        if tgbot:
            tgbot.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator


def chataction(**args):
    def decorator(func):
        if bot:
            bot.add_event_handler(func, events.ChatAction(**args))
        if CILIK2:
            CILIK2.add_event_handler(func, events.ChatAction(**args))
        if CILIK3:
            CILIK3.add_event_handler(func, events.ChatAction(**args))
        if CILIK4:
            CILIK4.add_event_handler(func, events.ChatAction(**args))
        if CILIK5:
            CILIK5.add_event_handler(func, events.ChatAction(**args))
        if CILIK6:
            CILIK6.add_event_handler(func, events.ChatAction(**args))
        if CILIK7:
            CILIK7.add_event_handler(func, events.ChatAction(**args))
        if CILIK8:
            CILIK8.add_event_handler(func, events.ChatAction(**args))
        if CILIK9:
            CILIK9.add_event_handler(func, events.ChatAction(**args))
        if CILIK10:
            CILIK10.add_event_handler(func, events.ChatAction(**args))
        if CILIK11:
            CILIK11.add_event_handler(func, events.ChatAction(**args))
        if CILIK12:
            CILIK12.add_event_handler(func, events.ChatAction(**args))
        if CILIK13:
            CILIK13.add_event_handler(func, events.ChatAction(**args))
        if CILIK14:
            CILIK14.add_event_handler(func, events.ChatAction(**args))
        if CILIK15:
            CILIK15.add_event_handler(func, events.ChatAction(**args))
        if CILIK16:
            CILIK16.add_event_handler(func, events.ChatAction(**args))
        if CILIK17:
            CILIK17.add_event_handler(func, events.ChatAction(**args))
        if CILIK18:
            CILIK18.add_event_handler(func, events.ChatAction(**args))
        if CILIK19:
            CILIK19.add_event_handler(func, events.ChatAction(**args))
        if CILIK20:
            CILIK20.add_event_handler(func, events.ChatAction(**args))
        return func

    return decorator


def callback(**args):
    def decorator(func):
        if tgbot:
            tgbot.add_event_handler(func, events.CallbackQuery(**args))
        return func

    return decorator
