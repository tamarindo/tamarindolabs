$('#panelDisenoDesarrollo .panelvisible .iconoabp'). on('mouseenter', function() {
	$('#panelDisenoDesarrollo .panelinvisible ').show("slow");
    });

$('#panelDisenoDesarrollo .panelinvisible .bnt_retractil'). on('click', function() {
	$('#panelDisenoDesarrollo .panelinvisible ').hide("slow");
    });

$('#panelAdminwebsite .panelvisible .iconoabp'). on('mouseenter', function() {
	$('#panelAdminwebsite .panelinvisible ').show("slow");
    });

$('#panelAdminwebsite .panelinvisible .bnt_retractil'). on('click', function() {
	$('#panelAdminwebsite .panelinvisible ').hide("slow");
    });

$('#panelAppmoviles .panelvisible .iconoabp'). on('mouseenter', function() {
	$('#panelAppmoviles .panelinvisible ').show("slow");
    });

$('#panelAppmoviles .panelinvisible .bnt_retractil'). on('click', function() {
	$('#panelAppmoviles .panelinvisible ').hide("slow");
    });



// funcion generales


function renderizarEn(Rhtml,id_div)
{
	$('#'+id_div).html(Rhtml);
	$('#'+id_div).show();
}




function sendAjax(url, params, myCallback, args) {
    if (typeof args === "") {
        load_elem = "#load";
    } else {
        load_elem = args.load_elem;
    	}
    
    $(load_elem).show().html('Cargando...');
   
    if (typeof args === "undefined" || args.met === "get") {
        $.get(url, params).done(function(data) {
            myCallback(data);
            $(load_elem).fadeOut();
        }).fail(function(error) {
            console.log(error);
        });
    }  else if (args.met === "post") {
        $.post(url, params).done(function(data) {
            myCallback(data);
            $(load_elem).fadeOut();
        	}).fail(function(error) {
            console.log(error);
        	});
    	}
	}
