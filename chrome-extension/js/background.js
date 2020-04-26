var contextMenus = {};

contextMenus.fackTikContextMenu = 
    chrome.contextMenus.create(
        {
            "title":"Factik",
            "contexts":["selection"]
        },
        function (){
            if(chrome.runtime.lastError){
                console.error(chrome.runtime.lastError.message);
            }
        }
    );

chrome.contextMenus.onClicked.addListener(contextMenuHandler);

function contextMenuHandler(info, tab){
    if(info.menuItemId === contextMenus.fackTikContextMenu ){
        checkFact(info.selectionText);
        
    }
}


function checkFact(message){
    var url = "http://167.71.230.150:5000/api/getPrediction/?inputtext="+encodeURI(message);
    fetch(url).then(response => {
        return response.json()
    }).then(body=>{
        console.log(body);
        var fake = body[0].Percentage[0] * 100
        var truth = body[1].Percentage[0] * 100;
        if(fake>truth){
            window.alert(fake+"% Likely that it is false");
        }else{
            window.alert(truth+"% Likely that it is correct");
        }
    })
}