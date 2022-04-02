var search=document.getElementById('search-form')

function showResult(val){
    res=document.getElementById("result")
    res.innerHTML=''
    if(val==''){
        return;
    }
    let list=""
    fetch("https://kitsu.io/api/edge/anime/?filter[text]="+val).then(
        function(response){
            return response.json();
        }
        ).then(function(data){
            data=data['data'].slice(0,5)
            // data=data.slice(0,5)
            // console.log()
            for(i=0;i<data.length;i++){        
                list+="<li class='search-item'>"   
                list+='<ul><li><h6>'+data[i]['attributes']['canonicalTitle']+ '</h6></li>'
                list+='<li><h6>Status: '+data[i]['attributes']['status']+ '</h6></li>'
                list+='<li><h6>Air Date: '+data[i]['attributes']['startDate']+ '</h6></li></ul>'
                list+="<img src="+data[i]['attributes']['posterImage']['tiny']+" >"
                list+="</li>"
                list+='<hr>'
            }
            res.innerHTML="<ul>" +list+"</ul>"
        return true
    }).catch(function(err){
        console.warn("something went wring ",err)
        return  false
    })

}
var counter=0

search.addEventListener("input",()=>{
    if(counter%2==0){
        (showResult(search.value))
    }
    counter+=1
})


// search bar result hide and show


var searchBar=document.getElementById('searchbar')



searchBar.addEventListener("click",()=>{
    document.getElementById("result").hidden=false;
})

searchBar.addEventListener("mouseleave",()=>{
    document.getElementById('result').hidden=true;
})
