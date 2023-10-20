import streamlit as st
import speech_recognition as sr
import string
import sounddevice as sd
import wavio
import os


samples_directory = './samples'
if not os.path.exists(samples_directory):
    os.makedirs(samples_directory)


def read_audio(file):
    with open(file, "rb") as audio_file:
        audio_bytes = audio_file.read()
    return audio_bytes

def record(duration=5, fs=48000):
    sd.default.samplerate = fs
    sd.default.channels = 1
    myrecording = sd.rec(int(duration * fs))
    sd.wait(duration)
    return myrecording

def save_record(path_myrecording, myrecording, fs):
    wavio.write(path_myrecording, myrecording, fs, sampwidth=2)
    return None

filename = 'audio'

isl_gif=['any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'be careful',
                'can we meet tomorrow', 'did you book tickets', 'did you finish homework', 'do you go to office', 'do you have money',
                'do you want something to drink', 'do you want tea or coffee', 'do you watch TV', 'dont worry', 'flower is beautiful',
                'good afternoon', 'good evening', 'good morning', 'good night', 'good question', 'had your lunch', 'happy journey',
                'hello what is your name', 'how many people are there in your family', 'i am a clerk', 'i am bore doing nothing', 
                 'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i dont understand anything', 'i go to a theatre', 'i love to shop',
                'i had to say something but i forgot', 'i have headache', 'i like pink colour', 'i live in nagpur', 'lets go for lunch', 'my mother is a homemaker',
                'my name is john', 'nice to meet you', 'no smoking please', 'open the door', 'please call me later',
                'please clean the room', 'please give me your pen', 'please use dustbin dont throw garbage', 'please wait for sometime', 'shall I help you',
                'shall we go together tommorow', 'sign language interpreter', 'sit down', 'stand up', 'take care', 'there was traffic jam', 'wait I am thinking',
                'what are you doing', 'what is the problem', 'what is todays date', 'what is your father do', 'what is your job',
                'what is your mobile number', 'what is your name', 'whats up', 'when is your interview', 'when we will go', 'where do you stay',
                'where is the bathroom', 'where is the police station', 'you are wrong','address','agra','ahemdabad', 'all', 'april', 'assam', 'august', 'australia', 'badoda', 'banana', 'banaras', 'banglore',
'bihar','bihar','bridge','cat', 'chandigarh', 'chennai', 'christmas', 'church', 'clinic', 'coconut', 'crocodile','dasara',
'deaf', 'december', 'deer', 'delhi', 'dollar', 'duck', 'febuary', 'friday', 'fruits', 'glass', 'grapes', 'gujrat', 'hello',
'hindu', 'hyderabad', 'india', 'january', 'jesus', 'job', 'july', 'july', 'karnataka', 'kerala', 'krishna', 'litre', 'mango',
'may', 'mile', 'monday', 'mumbai', 'museum', 'muslim', 'nagpur', 'october', 'orange', 'pakistan', 'pass', 'police station',
'post office', 'pune', 'punjab', 'rajasthan', 'ram', 'restaurant', 'saturday', 'september', 'shop', 'sleep', 'southafrica',
'story', 'sunday', 'tamil nadu', 'temperature', 'temple', 'thursday', 'toilet', 'tomato', 'town', 'tuesday', 'usa', 'village',
'voice', 'wednesday', 'weight','please wait for sometime','what is your mobile number','what are you doing','are you busy']

arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's','t','u','v','w','x','y','z','_']

if __name__ == '__main__':
    st.title("Speech to Sign Language :smile:",anchor="center")
    st.image("./signlang.png",use_column_width=True)
    # st.write("This app converts speech to sign language. You can record your voice and convert it to sign language. You can also type your text and convert it to sign language.")
    intro = ''' This app converts speech to sign language. 
    You can record your voice and convert it to sign language. 
    You can also type your text and convert it to sign language.
    '''
    #write this intro text in middle of the page
    st.markdown("<h3 style='text-align: center;'>"+intro+"</h3>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("========================================================================================")
    add_selectbox = st.sidebar.selectbox("Which operation do you want to follow?", ("Record Audio","Text input","Sign to Speech"))
    if(add_selectbox=="Record Audio"):
        if st.button("Click to Record", key="record_button"):
                record_state = st.text("Recording...")
                duration = 5  # seconds
                fs = 48000
                myrecording = record(duration, fs)
                record_state.text(f"Saving sample as {filename}.mp3")
                path_myrecording = f"./samples/{filename}.mp3"

                save_record(path_myrecording, myrecording, fs)
                record_state.text(f"Done! Saved sample as {filename}.mp3")
                st.audio(read_audio(path_myrecording))

                record_state.text(f"Converting sample to text...")
                
                r = sr.Recognizer()
                with sr.AudioFile(path_myrecording) as source:
                    audio = r.record(source)
                    
                text = r.recognize_google(audio)
                text = text.lower()
            
                for c in string.punctuation:
                    text = text.replace(c, "")
                record_state.text(f"Done! Converted sample to text.")
                # st.write(text)

                if text in isl_gif:
                    #load gid on app
                    st.image(f'./ISL_Gifs/{text}.gif')
                else:
                    #remove spaces from the text
                    stext = [char for char in text]
                    #if we get any space in the text then convert that space to underscore
                    for i in range(len(stext)):
                        if stext[i] == ' ':
                            stext[i] = '_'
                    for i in stext:
                        if i in arr:
                            st.image(f'./letters/{i}.jpg',use_column_width=True)
                        else:
                            st.text_area("Text", text, height=200)
                            break
                        
    elif(add_selectbox=="Text input"):        
            # st.markdown("<h1 style='text-align: center;'>OR</h1>", unsafe_allow_html=True)
            #take text as an input and submit it
            text = st.text_input("Enter text here")
            if st.button("Submit"):
                if text in isl_gif:
                #load gid on app
                    st.image(f'./ISL_Gifs/{text}.gif')
                else:
                    #remove spaces from the text
                    stext = [char for char in text]
                    #if we get any space in the text then convert that space to underscore
                    for i in range(len(stext)):
                        if stext[i] == ' ':
                            stext[i] = '_'
                    for i in stext:
                        if i in arr:
                            st.image(f'./letters/{i}.jpg',use_column_width=True)
                        else:
                            st.text_area("Text", text, height=200)
                            break

    elif(add_selectbox=="Sign to Speech"):
        st.write("This feature is under development")

    st.write("========================================================================================")