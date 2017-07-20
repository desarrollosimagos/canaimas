$(document).ready(function() {
    var entero = "0123456789"
    $('#cedula_jefe,#cedula,#telefono').validar(entero);
    var TUbch = $('#tabla_ubch').dataTable({
        "iDisplayLength": 5,
        "iDisplayStart": 0,
        "sPaginationType": "full_numbers",
        "aLengthMenu": [5, 10, 20, 30, 40, 50],
        "oLanguage": {"sUrl": "/static/js/es.txt"},
        "aoColumns": [
            {"sClass": "registro center", "sWidth": "8%"},
            {"sClass": "registro center", "sWidth": "25%"},
            {"sClass": "registro center", "sWidth": "8%"},
            {"sClass": "registro center", "sWidth": "15%"},
            {"sClass": "registro center", },
            {"sWidth": "3%", "bSortable": false, "sClass": "center sorting_false", "bSearchable": false}
        ]
    });


    $('#cedula').change(function(){
        var este = $(this)
        var cedula = este.val()
        $.get("http://consultaelectoral.bva.org.ve/cedula="+cedula, function(data) {
            $('#p_nombre').val(data[0].p_nombre)
            $('#s_nombre').val(data[0].s_nombre)
            $('#p_apellido').val(data[0].p_apellido)
            $('#s_apellido').val(data[0].s_apellido)
            $('#cod_ubch').val(data[0].cod_nuevo)
            $('#ubch').val(data[0].c_votacion)
        },'json').fail(function() {
            apprise('<span style="color:#FF0000;fotn-wight:bold">Esta C&eacute;dulano no se encuentra registrada en el CNE</span>', {'textOk': 'Aceptar'}, function() {
                este.parent('div').addClass('has-error')
                este.focus().select()
                $('#p_nombre,#s_nombre,#p_apellido,#s_apellido,#cod_ubch,#ubch').val('')
            });
        }); ;
    })
    
    $('#cedula_jefe').change(function(){
        var este  = $(this)
        var cedula = este.val()
        TUbch.fnClearTable();
        $.get("http://172.16.3.99:8000/ubch/cedula="+cedula, function(data) {
            $('#nombre_jefe').val(data[0].nombre)
            $('#cod_ubch_jefe').val(data[0].cod_ubch)
            $('#ubch_jefe').val(data[0].nom_ubch)
            $('#add.nuevo').css('display','block')
        },'json').fail(function() {
            apprise('<span style="color:#FF0000;fotn-wight:bold">Esta C&eacute;dulano pertenece a un jefe de patrulla</span>', {'textOk': 'Aceptar'}, function() {
                este.parent('div').addClass('has-error')
                este.focus().select()
                $('#nombre_jefe').val('')
                $('#cod_ubch_jefe').val('')
                $('#ubch_jefe').val('')
                $('#add.nuevo').css('display','none');
                $('div#div_registro').slideUp(1000);
                $('div#div_lista').slideDown(1000);
            });
        });    
        $.get("http://172.16.3.99:8000/ubch/lista/cedula_jefe="+cedula, function(data) {
            
            $.each(data, function(i, obj) {
                var eli = '<img class="eliminar" id ="'+obj.id+'" style="width:24px;height:24px;cursor:pointer"  src="/static/img/eliminar.png" />';
                var nombres = obj.p_nombre+' '+obj.s_nombre+' '+obj.p_apellido+' '+obj.s_apellido
                TUbch.fnAddData([obj.cedula, nombres,obj.telefono,obj.cod_ubch,obj.ubch,eli]);
            });
        },'json');
    })
    
    $('#registrar').click(function(){
        var $cedula = $('#cedula')
        var $telefono = $('#telefono')
        var $twitter = $('#twitter')
        if ($cedula.val() === null || $cedula.val().length === 0 || /^\s+$/.test($cedula.val())) {
           
            apprise('<span style="color:#FF0000;fotn-wight:bold">Debe indicar el n&uacute;mero de C&eacute;dula</span>', {'textOk': 'Aceptar'}, function() {
                $cedula.parent('div').addClass('has-error');
                $cedula.focus();
            });
            
        }else  if ($telefono.val() == '') {
            apprise('<span style="color:#FF0000;fotn-wight:bold">Debe indicar el n&uacute;mero de Tel&eacute;fono</span>', {'textOk': 'Aceptar'}, function() {
                $telefono.parent('div').addClass('has-error');
                $telefono.focus();
            });
            
        }else{
            $('#p_nombre,#s_nombre,#p_apellido,#s_apellido,#cod_ubch,#ubch').prop('disabled',false)
            $.post( "", $("#frmregistro").serialize()+'&accion=guardar', function(response){
                $('#p_nombre,#s_nombre,#p_apellido,#s_apellido,#cod_ubch,#ubch').prop('disabled',true)
                if (response['cedula'] == 'existe') {
                    apprise('<span style="color:#FF0000;fotn-wight:bold">Este n&uacute;mero de C&eacute;dula ya se encuentra registrado</span>', {'textOk': 'Aceptar'}, function() {
                        $cedula.parent('div').addClass('has-error');
                        $cedula.focus().select();
                    });
                }else if (response['save'] == 'ok') {
                    var cedula = $('#cedula').val()
                    var nombres = $('#p_nombre').val()+' '+$('#s_nombre').val()+' '+$('#p_apellido').val()+' '+$('#s_apellido').val()
                    var telefono = $('#telefono').val()
                    var twitter = $('#twitter').val()
                    var cod_ubch = $('#cod_ubch').val()
                    var ubch = $('#ubch').val()
                    var id = response['id']
                    apprise('<span style="color:#059102;fotn-wight:bold">El registro se guardo sastifactoriamente', {'textOk': 'Aceptar'}, function() {
                        var eli = '<img class="eliminar" id ="'+id+'" style="width:24px;height:24px;cursor:pointer"  src="/static/img/eliminar.png" />';
                        TUbch.fnAddData([cedula, nombres,telefono,cod_ubch,ubch,eli]);
                        $('div#div_registro').slideUp(1000);
                        $('div#div_lista').slideDown(1000);
                    });
                    
        
                }
            },'json');
        }
        
    });
    
    $('#add.nuevo').click(function(){
        $(this).css('display','none')
        
        $('div#div_lista').slideUp(1000);
        $('div#div_registro').slideDown(1000,function(){
            $('#cedula').focus();
        });
        
    });
    
    $('#tabla_ubch').on('click', 'img.eliminar', function() {
        var id_reg = $(this).attr('id')
        var padre      = $(this).closest('tr');
        var nRow       = padre[0];
        $.post("", {'id_reg':id_reg,csrfmiddlewaretoken: '{{ csrf_token }}'	,'accion':'eliminar'}, function(response) {
            if (response['delete'] == 'ok') {
                TUbch.fnDeleteRow(nRow);
            }
        });
    })
});
