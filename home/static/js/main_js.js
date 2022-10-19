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
    document.getElementById('conversation').innerHTML = ''
    var header;
    header = document.getElementById('chat-heading');
    header.innerText = subject_name;
    var box = document.getElementById('reply');
    if (box == null){
    var html = '<div class="row reply"><div class="col-sm-11 col-xs-11 reply-main"><textarea class="form-control" rows="1" id="comment"></textarea></div><div class="col-sm-1 col-xs-1 reply-send"><i class="fa fa-send fa-2x" aria-hidden="true" onClick="sendMessage()"></i></div></div>'
    get_messages(subject_name,'getmessage')
    }
    document.getElementById('con-box').innerHTML += html
    
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
function addRight(sender,message){
    textcontainer = document.createElement("div")
    textcontainer.classList.add('row')
    textcontainer.classList.add('message-body')
    textspan = document.createElement('div')
    textspan.classList.add('col-sm-12')
    textspan.classList.add('message-main-sender')
    senderp  =  document.createElement('span')
    senderp.classList.add('sender')
    senderp.innerHTML = String(sender)
    var textp = document.createElement('p')
    textp.classList.add('message-text')
    textp.innerHTML = String(message)
    senderp.appendChild(textp)
    textspan.appendChild(senderp)
    textcontainer.appendChild(textspan)
    document.getElementById('conversation').appendChild(textcontainer)
}
function addLeft(sender,message){
    textcontainer = document.createElement("div")
    textcontainer.classList.add('row')
    textcontainer.classList.add('message-body-receiver')
    textspan = document.createElement('div')
    textspan.classList.add('col-sm-12')
    textspan.classList.add('message-main-receiver')
    senderp  =  document.createElement('span')
    senderp.classList.add('receiver')
    senderp.innerHTML = String(sender)
    var textp = document.createElement('p')
    textp.classList.add('message-text')
    textp.innerHTML = String(message)
    senderp.appendChild(textp)
    textspan.appendChild(senderp)
    textcontainer.appendChild(textspan)
    document.getElementById('conversation').appendChild(textcontainer)
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

function sendMessage(){
    message = document.getElementById('comment').value
    console.log(message)
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