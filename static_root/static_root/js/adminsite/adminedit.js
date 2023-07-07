jQuery(document).ready(function() {  
    // $('.hasTooltip').tooltip();
console.log("HELLO")
var myELl=document.getElementById('parent').children;
console.log($('.stud').text)
if(myELl){
        for(var i=0;i<myELl.length;i++){
             var temp=myELl[i].getAttribute('id');
             console.log(temp)

}
}
    $('tbody').on('click', '.edit', function() {
        $(".tooltip").tooltip("hide");
     
        // if(myELl){
        //     for(var i=0;i<myELl.length;i++){
        //     var temp=myELl[i].getAttribute('id');
        //     console.log(temp)
        //     if(temp=="s1"){
        //         $('.edittext').attr('contenteditable','true');
        //     }
            
        //     }
        //     }
        $(".edittext").attr("id",)
        $("td").removeAttr("title");
     
     }); 
    //  $(".edit").attr("class","edit"+count);
});




