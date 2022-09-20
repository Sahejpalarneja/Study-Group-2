var user;
var subject;
var send_url = 'sendmessage'
var csrf_token;
function set_token(token){
    csrf_token = token
}
function set_user(current_user){
    user = current_user
}
function set_subject(current_subject){
    subject = current_subject
}
function chatClicked(subject_name)
{
    set_subject(subject_name)
    document.getElementById('chatbox').innerHTML = ''
    var header;
    header = document.getElementById('chatview_nav');
    header.innerText = subject_name;
    var box = document.getElementById('inputbox');
    if (box == null){
    var html = '<input type="text" class="form-control form-control-lg " id="inputbox" placeholder="Type message" ><a class="ms-3" href="#!"><i class="bi bi-send " id="sendButton" onClick="sendMessage()"></i></a>'
    document.getElementById('chatbox').innerHTML += html
    get_messages(subject_name,'getmessage')
    }
    
}
function get_messages(subject_name,url){
    $.ajax(
        {
            type:'GET',
            url:url,
            data:{
                subject :subject_name,
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            success:function(data){
                addMessages(data)
            }

        }
    )

}
function addMessages(sub_messages){
    sub_messages = sub_messages.replaceAll("'",'"') ;
    sub_messages = JSON.parse(sub_messages)
    for(let i =0;i<sub_messages.length;i++)
    {
        var sender = sub_messages[i]['sender']
        if (sender === user){
            addRight(sub_messages[i]['sender'],sub_messages[i]['text'])
        }
        else{
            addLeft(sub_messages[i]['sender'],sub_messages[i]['text'])
        }
    }
}
function addRight(sender,message){
    textright = document.createElement("div")
    textright.classList.add('col-6')
    textright.classList.add('msg')
    textright.classList.add('right')
    var senderp  =  document.createElement('p')
    senderp.innerHTML = String(sender)
    var textp = document.createElement('p')
    textp.innerHTML = String(message)
    textright.appendChild(senderp)
    textright.appendChild(textp)
    document.getElementById('chatbox').appendChild(textright)
}
function addLeft(sender,message){
    var textleft = document.createElement("div")
    textleft.classList.add('col-6')
    textleft.classList.add('msg')
    textleft.classList.add('left')
    var senderp  =  document.createElement('p')
    senderp.innerHTML = sender
    var textp = document.createElement('p')
    textp.innerHTML = message
    textleft.appendChild(senderp)
    textleft.appendChild(textp)
    document.getElementById('chatbox').appendChild(textleft)
}
function addMessages(sub_messages){
    sub_messages = sub_messages.replaceAll("'",'"') ;
    console.log(sub_messages)
    sub_messages = JSON.parse(sub_messages)
    for(let i =0;i<sub_messages.length;i++)
    {
        var sender = sub_messages[i]['sender']
        if (sender === user){
            addRight(sub_messages[i]['sender'],sub_messages[i]['text'])
        }
        else{
            addLeft(sub_messages[i]['sender'],sub_messages[i]['text'])
        }
    }
}

function sendMessage(){
    message = document.getElementById('inputbox').value
    addRight(user,message)
    $.ajax(
        {
            type:"POST",
            url:send_url,
            data:{
                message:message,
                sender:user,
                subject:subject,
                csrfmiddlewaretoken: csrf_token
            },
            success:function(data){
                console.log("sent")
            }
        }
    )
}