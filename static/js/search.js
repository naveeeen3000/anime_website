console.log("IN THE JS")

function showResult(val){
    console.log("runnig//")
    res=document.getElementById("result")
    res.innerHTML=''
    if(val==''){
    return;
    }

    let list=''
    fetch("https://kitsu.io/api/edge/anime/?filter[text]="+val).then(
        function(response){
            return response.json();
        }
    ).then(function(data){
        for(i=0;i<data.length;i++){
            list+='<li>'+data[i]+ '</li>'
        }
        res.innerHTML='<ul>' +list +'</ul>'
        return true
    }).catch(function(err){
        console.warn("something went wring ",err)
        return  false
    })

}