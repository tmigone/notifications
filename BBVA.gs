function agentBBVA()
{
    var labelThreads = GmailApp.getUserLabelByName("BBVA").getThreads();
    
    for (var i = 0; i < labelThreads.length; i++)
        if(labelThreads[i].isUnread())
        {
            var messages = labelThreads[i].getMessages();
            for (var j = 0; j < messages.length; j++)
                if(messages[j].isUnread())
                {
                    // Debito directo
                    if(messages[j].getSubject() == "Mensajes y avisos por e-mail - Servicios")
                    {
                        sendNotification("Debito", debitParse(messages[j].getBody()));
                        messages[j].markRead();
                    }
                    
                    // Tarjeta de credito
                    if(messages[j].getSubject() == "Nuevos consumos de sus tarjetas Visa")
                    {
                        sendNotification("Credito", creditParse(messages[j].getBody()));
                        messages[j].markRead();
                    }
                }
        }
}


function debitParse(body)
{
    var text = body.slice(body.search("El servicio"), body.search("499/5"));
    
    var service = text.slice(12, text.search("con")-1).trim();
    var amount = text.slice(text.search("por")+5, Math.max(text.search(", con"), text.search(", venció"), text.search(", vence"))).trim();
    var outcome = text.search("fue debitado") > 0 ? "Debitado" : (text.search("será debitado") > 0 ? "Por debitar" : (text.search("ser debitado") > 0 ? "Fondos insuficientes" : "Error"));
    
    return "Servicio: " + service + "\nMonto: $" + amount + "\nEstado: " + outcome;
}

function creditParse(body)
{
    var text = body.slice(body.search("establecimiento"), body.search("horas"));
    
    var service = text.slice(16, text.search("por")-1).trim();
    var amount = text.slice(text.search("por")+5, text.search(", el")).trim();
    var outcome = body.search("se ha registrado una autorizacion") > 0 ? "Ok" : "Error";
    
    return "Servicio: " + service + "\nMonto: $" + amount + "\nEstado: " + outcome;
}

function sendNotification(title, message)
{
    var payload =
    {
        "token": "adn3bgkZG1ywNi8YmWcFREjqPsov9a",
        "user": "u8q5UGNSFJoKpJaX7XyaNYHzpoAKzG",
        "message": message,
        "title": title
    };
    
    var options =
    {
        "method" : "post",
        "payload" : payload
    };
    UrlFetchApp.fetch("https://api.pushover.net/1/messages.json", options);
}



