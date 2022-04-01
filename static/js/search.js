var search=document.getElementById('search-form')

function showResult(val){
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
            data=data['data']
            console.log()
            for(i=0;i<data.length;i++){           
                // list+='<li><h6>'+data[i]['attributes']['canonicalTitle']+ '</h6></li>'
                list+="<img src="+data[i]['attributes']['posterImage']['tiny']+" >"
            }
            res.innerHTML="<ul class='list-item'>" +list +'</ul>'
        return true
    }).catch(function(err){
        console.warn("something went wring ",err)
        return  false
    })

}
var counter=0

search.addEventListener("input",(val)=>{
    if(counter%2==0){
        (showResult(search.value))
    }
    counter+=1
})
