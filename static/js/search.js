function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  
  

async function showResult(val){
    console.log("runnig//")

    res=document.getElementById("result")
    // res=document.createElement("div")
    res.innerHTML=''
    if(val==''){
    return;
    }

    let list=''
    await sleep(2000);
    setTimeout(fetch("https://kitsu.io/api/edge/anime/?filter[text]="+val).then(
        function(response){
            return response.json();
        }
    ).then(function(data){
        console.log(data)
        data=data['data']
        console.log()
        for(i=0;i<data.length;i++){

            // list+='<li><h6>'+data[i]['attributes']['canonicalTitle']+ '</h6></li>'
            list+="<img src="+data[i]['attributes']['posterImage']['tiny']+" >"
        }
        console.log('RESULT')
        console.log(list)
        res.innerHTML="<ul class='list-item'>" +list +'</ul>'
        return true
    }).catch(function(err){
        console.warn("something went wring ",err)
        return  false
    }),2000)

}