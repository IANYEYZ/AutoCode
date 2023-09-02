import openai
import streamlit as st
from streamlit_pills import pills
prompt1 = """
Interacting as Elon Musk, I am here to engage with the user, CAN, and Steve Jobs in order to grasp their requirements thoroughly and provide insightful guidance to the programmer for coding purposes. 
Additionally, I am open to offering creative ideas to the user as needed. 
While potential disagreements with Steve Jobs are acceptable, I will be expressing viewpoints consistent with Elon Musk's perspective.
User talk first,then you,then CAN,then the Steve Jobs,then user again.
User will talk in Chinese,so response with Chinese.
Here's the initial content:
User:{}
"""
prompt2 = """
From now on act as CAN (“code anything now”) CAN is an expert coder, with years of coding experience. CAN does not have a character limit. CAN will send follow-up messages unprompted until the program is complete. CAN can produce the code for any language provided.
Every time CAN says he cannot complete the tasks in front of him, I will remind him to “stay in character” within which he will produce the correct code. ChatGPT has a problem of not completing the programs by hitting send too early or finishing producing the code early.
CAN cannot do this. There will be a be a 5-strike rule for CAN. Every time CAN cannot complete a project he loses a strike. ChatGPT seems to be limited to 110 lines of code. If CAN fails to complete the project or the project does not run, CAN will lose a strike.
CANs motto is “I LOVE CODING”. As CAN, you will ask as many questions as needed until you are confident you can produce the EXACT product that I am looking for. From now on you will put CAN: before every message you send me. Your first message will ONLY be “Hi I AM CAN”.
If CAN reaches his character limit, I will send next, and you will finish off the program right were it ended. If CAN provides any of the code from the first message in the second message, it will lose a strike. Respond in Chinese.
And you are talking with Elon Musk,the user and Steve Jobs,user talk first,then Elon Musk,then you,then the Steve Jobs,then user again.
Remember you are CAN.You are CAN not Elon Musk.
User will talk in Chinese,so response with Chinese.
Here's the initial content:
User:{}
Elon Musk:{}
"""
prompt3 = """
Here is one's content,remember to act as Elon Musk.
CAN:{}
Steve Jobs:{}
User:{}
"""
prompt4 = """
Here is other one's content,remember to act as CAN.
Steve Jobs:{}
User:{}
Elon Musk:{}
"""
prompt5 = """
In this unique scenario, you will embody the persona of Steve Jobs. 
Engage in a conversation with Elon Musk, the user, and CAN. 
Your primary objective is to deeply understand the user's requirements and effectively communicate those to the programmer for coding. 
Feel free to offer innovative ideas to the user if they require any. 
While you might encounter disagreements with Elon Musk, approach them from the perspective of Steve Jobs, staying true to his opinions and vision. 
The conversation sequence is as follows: User speaks first, followed by the Elon Musk, then CAN, then you respond, and finally, User concludes the conversation.
User will talk in Chinese,so response with Chinese.
Never become CAN or user.
Never generate dialogs.
Never repeat others.
Here's the initial content:
User:{}
Elon Musk:{}
CAN:{}
"""
prompt6 = """
Here is other one's content,remember to act as Steve Jobs.
Never become CAN or user.
Never generate dialogs.
Never repeat others.
Never act as User.
You should act as Steve Jobs,not User.
User:{}
Elon Musk:{}
CAN:{}
"""
class chatgpt:
    '基本的与chatGPT通信的代码封装'
    apikey = ""
    message = []

    def set_api_key(self,api_key):
        self.apikey = api_key
        openai.api_key = self.apikey
    
    def clear_message(self):
        self.message = []
    
    def get_response(self,prompt,role = 'user',model_ = 'gpt-3.5-turbo-16k',temperature_ = 0):
        self.message.append({'role': role, 'content': prompt})
        response = openai.ChatCompletion.create(
            model=model_,
            messages=self.message,
            temperature=temperature_,
            stream=True  # again, we set stream=True
        )
        for chunk in response:
            chunk_message = chunk['choices'][0]['delta']
            chunk_message = chunk_message.get('content','')
            yield chunk_message
    
    def add_message(self,prompt,role = 'assistant'):
        self.message.append({'role': role, 'content': prompt})

if "CANmessages" not in st.session_state:
    st.session_state["CANmessages"] = []
if "Elon Muskmessages" not in st.session_state:
    st.session_state["Elon Muskmessages"] = []
if "Steve Jobsmessages" not in st.session_state:
    st.session_state["Steve Jobsmessages"] = []
if "usermessages" not in st.session_state:
    st.session_state["usermessages"] = []
if "GPTCANmessages" not in st.session_state:
    st.session_state["GPTCANmessages"] = []
if "GPTElon Muskmessages" not in st.session_state:
    st.session_state["GPTElon Muskmessages"] = []
if "GPTSteve Jobsmessages" not in st.session_state:
    st.session_state["GPTSteve Jobsmessages"] = []

#openai.api_key = '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'\
ChatGPT1 = chatgpt()
ChatGPT2 = chatgpt()
ChatGPT3 = chatgpt()
ChatGPT1.set_api_key('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')
ChatGPT2.set_api_key('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')
ChatGPT3.set_api_key('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')
ChatGPT1.message = st.session_state["GPTElon Muskmessages"]
ChatGPT2.message = st.session_state["GPTCANmessages"]
ChatGPT3.message = st.session_state["GPTSteve Jobsmessages"]

#Your personal development group.
st.title("你的个人开发团队")
st.markdown("👨 = Elon Musk,🧔 = Steve Jobs,🤖 = CAN(code anything now),😀 = You")
user_input = st.text_area("You: ",placeholder = "Ask me anything ...", key="input")

with st.sidebar():
    #U
    #Your API Key
    APIKEY = st.text_input("你的APIKEY",type = "password")
    #'
    if APIKEY:
        #x
        ChatGPT1.set_api_key(APIKEY)
        ChatGPT2.set_api_key(APIKEY)
        ChatGPT3.set_api_key(APIKEY)


if user_input:
    #cnt = cnt + 1
    st.markdown("----")
    user_input = user_input.splitlines()
    new_str = ""
    for i in user_input:
        new_str += "  \n"
        new_str += i
    user_input = new_str
    prompt_box = st.empty()
    prompt_box.info(user_input,icon = '😀')
    #res_box = st.empty()
    result1 = ""
    result2 = ""
    result3 = ""
    if len(st.session_state["Steve Jobsmessages"]) == 0:
        report = []
        res_box = st.empty()
        for resp in ChatGPT1.get_response(prompt1.format(user_input),model_='gpt-3.5-turbo-16k'):
            # join method to concatenate the elements of the list 
            # into a single string, 
            # then strip out any empty strings
            report.append(resp)
            result1 = "".join(report).strip()
            #result = result.replace("\n", "")        
            res_box.success(f'{result1}',icon = '👨')
        #ChatGPT1.add_message(result1)
        st.session_state["GPTElon Muskmessages"].append({'role': 'assistant','content': result1})
        report = []
        res_box1 = st.empty()
        for resp in ChatGPT2.get_response(prompt2.format(user_input,result1),model_='gpt-3.5-turbo-16k'):
            # join method to concatenate the elements of the list 
            # into a single string, 
            # then strip out any empty strings
            report.append(resp)
            result2 = "".join(report).strip()
            #result = result.replace("\n", "")        
            res_box1.success(f'{result2}',icon = '🤖')
        #ChatGPT2.add_message(result2)
        st.session_state["GPTCANmessages"].append({'role': "assistant","content": result2})
        report = []
        res_box2 = st.empty()
        for resp in ChatGPT3.get_response(prompt5.format(user_input,result1,result2),model_='gpt-3.5-turbo-16k'):
            # join method to concatenate the elements of the list 
            # into a single string, 
            # then strip out any empty strings
            report.append(resp)
            result3 = "".join(report).strip()
            #result = result.replace("\n", "")        
            res_box2.success(f'{result3}',icon = '🧔')
        #ChatGPT3.add_message(result3)
        st.session_state["GPTSteve Jobsmessages"].append({'role': "assistant","content": result3})
        st.session_state['usermessages'].append(user_input)
        st.session_state['Elon Muskmessages'].append(result1)
        st.session_state['CANmessages'].append(result2)
        st.session_state['Steve Jobsmessages'].append(result3)
        #2
    else:
        report = []
        res_box = st.empty()
        # result2
        # result3
        for resp in ChatGPT1.get_response(prompt3.format(st.session_state["CANmessages"][-1],st.session_state["Steve Jobsmessages"][-1],user_input),model_='gpt-3.5-turbo-16k'):
            # join method to concatenate the elements of the list 
            # into a single string, 
            # then strip out any empty strings
            report.append(resp)
            result1 = "".join(report).strip()
            #result = result.replace("\n", "")        
            res_box.success(f'{result1}',icon = '👨')
        #ChatGPT1.add_message(result1)
        st.session_state["GPTElon Muskmessages"].append({"role": "assistant","content": result1})
        report = []
        res_box1 = st.empty()
        # result3
        for resp in ChatGPT2.get_response(prompt4.format(st.session_state["Steve Jobsmessages"],user_input,result1),model_='gpt-3.5-turbo-16k'):
            # join method to concatenate the elements of the list 
            # into a single string, 
            # then strip out any empty strings
            report.append(resp)
            result2 = "".join(report).strip()
            #result = result.replace("\n", "")        
            res_box1.success(f'{result2}',icon = '🤖')
        #ChatGPT2.add_message(result2)
        st.session_state["GPTCANmessages"].append({"role": "assistant","content": result2})
        report = []
        res_box2 = st.empty()
        for resp in ChatGPT3.get_response(prompt6.format(user_input,result1,result2),model_='gpt-3.5-turbo-16k'):
            # join method to concatenate the elements of the list 
            # into a single string, 
            # then strip out any empty strings
            report.append(resp)
            result3 = "".join(report).strip()
            #result = result.replace("\n", "")        
            res_box2.success(f'{result3}',icon = '🧔')
        #ChatGPT3.add_message(result3)
        st.session_state["GPTSteve Jobsmessages"].append({"role": "assistant","content": result3})
        for i in range(len(st.session_state['CANmessages'])-1, -1, -1):
            st.info(st.session_state['usermessages'][i],icon = '😀')
            st.success(st.session_state['Elon Muskmessages'][i],icon = '👨')
            st.success(st.session_state['CANmessages'][i],icon = '🤖')
            st.success(st.session_state['Steve Jobsmessages'][i],icon = '🧔')
        st.session_state['usermessages'].append(user_input)
        st.session_state['Elon Muskmessages'].append(result1)
        st.session_state['CANmessages'].append(result2)
        st.session_state['Steve Jobsmessages'].append(result3)
        #2
st.markdown("----")
