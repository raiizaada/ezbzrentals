$(document).ready(function() {
    $("#RentalID").on('change', function() {
        var RentalID = $(this).val(); 
       
        
        $.ajax({                     
            type: "POST",
            url: ("/rentals"),
            data: {
                'rental_id': RentalID,      
                
            },
            success: function (data) {   
                
                $("#RentalResponse").html(data); 
                $("#RentalResponseHide*").css('display', 'none')
            }
        });
    });
 

});
