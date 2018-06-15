function stworz_tabele_lotow()
{
    let data = document.forms["filtr_data"]["data_lotu"].value;
    if (data == "") {
        return;
    }
    
    let rest_api_zalogi = new XMLHttpRequest();
    let zalogi_url = "http://127.0.0.1:8000/rest/zalogi/";
    
    var json_zalogi;
    rest_api_zalogi.onreadystatechange = function()
    {
        if (this.readyState == 4 && this.status == 200)
        {
            window.json_zalogi = JSON.parse(this.responseText);
        }
    }
    
    rest_api_zalogi.open("GET", zalogi_url, false);
    rest_api_zalogi.send();
    
    let rest_api_loty = new XMLHttpRequest();
    let loty_url = "http://127.0.0.1:8000/rest/loty/" + data + "/";
    
    rest_api_loty.onreadystatechange = function()
    {
        let html = ""
        if (this.readyState == 4 && this.status == 200)
        {
            let json_loty = JSON.parse(this.responseText);
            if (json_loty.length > 0)
            {
                html += "<table><tr>"
                html += "<th>Lotnisko startowe</th>"
                html += "<th>Lotnisko docelowe</th>"
                html += "<th>Czas wylotu</th>"
                html += "<th>Czas lądowania</th>"
                html += "<th>Kapitan załogi</th>"
                html += "</tr>"
                for(let i = 0; i < json_loty.length; i++)
                {
                    html += "<tr><td>"
                    html += json_loty[i].lotnisko_startowe;
                    html += "</td><td>"
                    html += json_loty[i].lotnisko_docelowe;
                    html += "</td><td>"
                    html += json_loty[i].czas_startu;
                    html += "</td><td>"
                    html += json_loty[i].czas_ladowania;
                    html += "</td><td>"
                    html += "<form><select name=select_" + i;
                    html += " onchange=\"zmien_zaloge(" + json_loty[i].id + ", ";
                    html += "select_" + i + ".value)\">"
                    html += "<option value=\"-1\"></option>";
                    for (let j = 0; j < window.json_zalogi.length; j++)
                    {
                        html += "<option value=\"" + window.json_zalogi[j].id + "\"";
                        if (json_loty[i].zaloga != null && json_loty[i].zaloga.id === window.json_zalogi[j].id)
                        {
                            html += " selected";
                        }
                        html += ">" + window.json_zalogi[j].imie_i_nazwisko_kapitana + "</option>";
                    }
                    html += "</select></form></td></tr>"
                }
                html += "</table>"
            }
            
            document.getElementById("div_tabela_lotow").innerHTML = html;
        }
    };
    
    rest_api_loty.open("GET", loty_url, false);
    rest_api_loty.send();
}

function zmien_zaloge(lot_id, zaloga_id)
{
    if (zaloga_id == -1)
    {
        ItemJSON = '{"id": ' + lot_id + ', "zaloga": "None"}';
    }
    else
    {
        ItemJSON = '{"id": ' + lot_id + ', "zaloga": "' + zaloga_id + '"}';
    }
    let rest_api_zmiany_zalogi = new XMLHttpRequest();
    let zmiana_zalogi_url = "http://127.0.0.1:8000/rest/zaloga_lotu/";
    
    rest_api_zmiany_zalogi.onreadystatechange = function() {}
    
    rest_api_zmiany_zalogi.open("PATCH", zmiana_zalogi_url, false);
    rest_api_zmiany_zalogi.setRequestHeader("Content-Type", "application/json");
    rest_api_zmiany_zalogi.setRequestHeader("X-CSRFToken", CSRF_TOKEN);
    rest_api_zmiany_zalogi.send(ItemJSON);
    if (rest_api_zmiany_zalogi.status != 201)
    {
        alert("Błąd: ta załoga uczestniczy już (w tym samym czasie) w innym locie!");
        console.log(rest_api_zmiany_zalogi)
    }
    stworz_tabele_lotow()
}


