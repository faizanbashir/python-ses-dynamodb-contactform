$(function(){
 
    $('#serverless-form').submit(function(e){
        e.preventDefault();
        var formdata = toJSONString(this);
        console.log(formdata);
        $.ajax({
            type: "POST",
            url: URL,
            dataType: "json",
            contentType: "application/json",
            data: formdata,
            beforeSend: function(data) {
                $('#submit').attr('disabled', true);
                $('#status').html('<i class="fa fa-refresh fa-spin"></i> Sending Mail...').show();
            },
            success: function(data) {
                console.log(data);
                $('#status').text('Mail sent!').show();
                $('#submit').removeProp('disabled');
            },
            error: function(jqXHR, textStatus, errorThrown) {
                $('#status').text('Mail sending Failed').show();
                $('#submit').removeProp('disabled');
            }
        });
    });

    function toJSONString (form) {
		var obj = {};
		var elements = form.querySelectorAll("input, select, textarea");
		for(var i = 0; i < elements.length; ++i) {
			var element = elements[i];
			var name = element.name;
			var value = element.value;
			if(name) {
				obj[name] = value;
			}
        }
        return JSON.stringify(obj);
    }
});
