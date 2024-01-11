import mysql.connector
import streamlit as st
from streamlit_option_menu  import option_menu 
database=mysql.connector.connect(
  host="localhost",
  user="root",
  password="localhost920",
  database="mydb",
  auth_plugin='mysql_native_password'
)
mycursor=database.cursor()
print("successfully connect")
st.title("Welcome To  CloudBlitz" + " "+ ":barely_sunny:");

option=st.sidebar.selectbox("Select And options",("Create Account","Update Account","Delete Account")) 
selected= option_menu(
menu_title=None,
options=["Account","Check Information",],
orientation="horizontal"
)
st.sidebar.header("About:-") 
st.sidebar.write('''
                 this project is created by pranay patil by using python language
                Display Your name in result With Perentage You Won
                Also Mentioned Lettet for your....             
             contact- pranaypatil024@gmai.com 
             
             Available for 24 hours 
                ''' 
                )

if selected=="Account":
    st.subheader("Fill The Information")
    if option=="Create Account":
        name=st.text_input("Enter Your Name",)
        email=st.text_input("Enter your Email",)
        if  name:
            st.warning("enter your email eg.@gmail.com")
        address=st.text_input("Enter Your Address") 
        qualification=st.text_input("Enter Your Qualification") 
        whatsapp=st.text_input("Enter Your Whatsapp Number") 
        status =st.radio("Select Your Gen",("Male","Female"))
        st.write("You selected",status)
   # nameinput=name
   # emailinput=email
        #if  name:
         #   st.warning("please enter your email eg.@gmail.com")
        if  email: 
            st.write("")
        if  address: 
            st.write()
            if st.button("Create"): 
             sql="insert into userss(name,email,address,qualification,whatsapp) values(%s,%s,%s,%s,%s)"
             val=(name,email,address,qualification,whatsapp)
             mycursor.execute(sql,val)
             database.commit()
             st.success("Account Created Successfully")
                
        
           
           
    if option=="Update Account":
                    st.subheader("Update Account")
                    id=st.number_input("Enter Account ID",min_value=1)
                    name=st.text_input("Enter New Name")
                    email=st.text_input("Enter New Email")        
                    if  st.button("Update"):
                     sql="update userss set name=%s, email=%s where id =%s"
                     val=(name,email,id) 
                     mycursor.execute(sql,val)
                     database.commit()
                     st.success("Record Update Successfully")
     
            
    if option=="Delete Account":
                    st.subheader("Delete Account")
                    st.number_input("Account ID",min_value=1) 
                    if st.button("Delete"):
                     sql="delete from userss where id =%s"
                     val=(id)
                     mycursor.execute(sql,val)
                     database.commit()
                     st.success("Record Deleted Successfully")
            
        
        
        
if selected=="Check Information":
               
               st.subheader("Read Accounts")   
               mycursor.execute("Select * from userss")
               result = mycursor.fetchall()
               for row in result:   
                st.write(row)
       
        
    
    
    
#contact_form ='''
#
#<form action="https://formsubmit.co/patilpranay024@gmail.com" method="POST">
#     <input type="hidden" name="_captcha" value="false">
#     <input type="text" name="name" placeholder="Your Name"required>
#     <input type="email" name="email" placeholder="Your email"required>
#     <textarea name ="message" placeholder="Your messege here" required></textarea>
#     <button type="submit">Send</button>
#</form>
#'''
#left_column, right_column = st.columns(2)
#with left_column:
   #     st.markdown(contact_form, unsafe_allow_html=True)
#with right_column:
   #     st.empty()
