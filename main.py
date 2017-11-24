import requests
import json
from json.decoder import JSONDecodeError
# import re

from constants import *
from config import *

# constants
BASE_URL = ""
GID = ""
PW = ""
COOKIES = dict()

def make_ajaxservlet_request(data):
    r = requests.post(BASE_URL+"/AjaxServlet",
        cookies=COOKIES,
        headers={"Connection":"keep-alive"},
        data=data)
    response = parse_ajaxservlet_json(r.text)
    return response


def make_longpollservlet_request():
    r = requests.post(BASE_URL+"/LongPollServlet",
        cookies=COOKIES,
        headers={"Connection":"keep-alive"})
    response = parse_ajaxservlet_json(r.text)
    return response


def parse_ajaxservlet_json(text):
    try:
        response = json.loads(text)
        if CAH_AjaxResponse_ERROR in response:
            LOG.error("Error detected in response: %s" % text)
            if response[CAH_AjaxResponse_ERROR] == True and CAH_AjaxResponse_ERROR_CODE in response:
                LOG.error("Error code found in response: %s" % text)
                return None
        return response
    except JSONDecodeError:
        LOG.error("JSON error in response: %s" % text)
        return None


def get_game_attributes(url):
    global COOKIES, GID, BASE_URL, PW
    # Split the URL into 2 pieces: the server URL and the game ID
    args = url.split("/game.jsp#game=")
    LOG.warning(str(args))
    if len(args) != 2:
        LOG.critical("Could not find all arguments from URL passed.")
        return False
    # Set server URL & game ID.
    BASE_URL = args[0]
    GID = args[1]
    return True


def register_user():
    global COOKIES, GID, BASE_URL, PW
    # Get cookies from game.jsp
    r = requests.get(BASE_URL+"/game.jsp")
    COOKIES = r.cookies
    # Make register request
    data = {CAH_AjaxRequest_OP:CAH_AjaxOperation_REGISTER,CAH_AjaxRequest_SERIAL:SERIAL,CAH_AjaxRequest_NICKNAME:NICKNAME}
    response =  make_ajaxservlet_request(data)
    LOG.warning(str(response))
    if not response or CAH_AjaxRequest_NICKNAME not in response:
        return False
    return True


def spectate_game():
    global COOKIES, GID, BASE_URL, PW
    data = {CAH_AjaxRequest_OP:CAH_AjaxOperation_SPECTATE_GAME,CAH_AjaxRequest_SERIAL:SERIAL,CAH_AjaxRequest_GAME_ID:GID}
    response =  make_ajaxservlet_request(data)
    LOG.warning(str(response))


def send_message(message):
    global COOKIES, GID, BASE_URL, PW
    data = {CAH_AjaxRequest_OP:CAH_AjaxOperation_GAME_CHAT,CAH_AjaxRequest_SERIAL:SERIAL,CAH_AjaxRequest_GAME_ID:GID,CAH_AjaxRequest_MESSAGE:message}
    response = make_ajaxservlet_request(data)
    LOG.warning(str(response))


def logout():
    global COOKIES, GID, BASE_URL, PW
    data = {CAH_AjaxRequest_OP:CAH_AjaxOperation_LOG_OUT,CAH_AjaxRequest_SERIAL:SERIAL}
    response =  make_ajaxservlet_request(data)
    LOG.warning(str(response))


def leave_game():
    global COOKIES, GID, BASE_URL, PW
    data = {CAH_AjaxRequest_OP:CAH_AjaxOperation_LEAVE_GAME,CAH_AjaxRequest_SERIAL:SERIAL,CAH_AjaxRequest_GAME_ID:GID}
    response =  make_ajaxservlet_request(data)
    LOG.warning(str(response))


#######################
# EVENT HANDLERS      #
#######################

def event_kick_bot(json_dict):
    # check if message says "?kick NICKNAME". If so, return True
    if CAH_LongPollResponse_MESSAGE in json_dict:
        message = json_dict[CAH_LongPollResponse_MESSAGE]
        if message.lower().strip() == "?kick %s" % NICKNAME:
            return True
    return False


def event_whomst(json_dict):
    # check if contains "who" and NICKNAME. If so, return True
    if CAH_LongPollResponse_MESSAGE in json_dict:
        message = json_dict[CAH_LongPollResponse_MESSAGE]
        message = message.lower()
        if "who" in message and NICKNAME.lower() in message:
            return True
    return False


def main():
    url = input("Game URL: ")
    # passwords not needed for spectators, eyes emoji
    PW = input("Password?: ")

    whom_replies = ["I am the king of this kingdom!",
                    "I'm a rabbit.",
                    "I'm an AI.",
                    "I'm an artificial intelligence, powered by a quantum computer.",
                    "I'm just the...facilitator for this game.",
                    "I'm sure you've got loooooots of questions. It just seems silly to have a big old chit-chat right now.",
                    "..."]

    # get cookies, game ID, server URL, register user, and spectate game
    if get_game_attributes(url) and register_user():
        spectate_game()

        ###############################
        # MAIN EVENT LISTENER LOOP    #
        ###############################
        stop_condition = False
        response_number = 0
        while not stop_condition:
            response = make_longpollservlet_request()
            LOG.warning(str(response))
            
            # Any response in the form of a list of dictionaries has an event.
            if isinstance(response, list):
                for json_dict in response:
                    if CAH_LongPollResponse_EVENT in json_dict:
                        event_type = json_dict[CAH_LongPollResponse_EVENT]

                        ################
                        # EVENT LIST   #
                        ################
                        if event_type == CAH_LongPollEvent_CHAT:
                            # CHAT EVENTS
                            if event_kick_bot(json_dict):
                                # Command to leave server - leave game & set stop condition
                                stop_condition = True
                                leave_game()
                            elif event_whomst(json_dict):
                                # Command to send introductory message
                                reply_num = response_number
                                if reply_num >= len(whom_replies):
                                    reply_num = len(whom_replies) - 1
                                send_message(whom_replies[reply_num])
                                response_number+=1

        #####################################
        # MAIN EVENT LISTENER LOOP COMPLETE #
        #####################################
        LOG.warning("COMPLETE")        


main()
