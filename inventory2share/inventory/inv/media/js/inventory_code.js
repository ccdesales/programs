$.ajaxSetup ({  
	cache: false  
});

$(document).ready(function() {
	
	function get_item_id(elem, prefix) {
		//Extract the item ID from an specific element given a prefix
		var id = elem.attr('id');
		var item_id = id.split(prefix)[1];
		return item_id;
	};
	
	function check_if_selected(item_id) {
		//Check item id checkbox if any of isexist or isreorder is checked
		is_exists  = $("#form_canvas .cell #isexist_"   + item_id).is(':checked');
		is_reorder = $("#form_canvas .cell #isreorder_" + item_id).is(':checked');
		
		var item = $("#form_canvas .cell #" + item_id);
		item.attr("checked", is_exists || is_reorder);
	};
	
	$("#form_canvas input[name^=isexist_]").change(function() {
		var item_id = get_item_id($(this), "isexist_");
		check_if_selected(item_id);
 	});
 	
	$("#form_canvas input[name^=isreorder_]").change(function() {
		var item_id = get_item_id($(this), "isreorder_");
		check_if_selected(item_id);
	});
 	
	$("input#ajax").click(function() {
		//var ajax_load = "<img src='img/load.gif' alt='loading...' />";
		var ajax_load = "<img style='width: 80px; height: 80px;' alt='AAA' src='/static/images/a.jpg' />";  
		  
		//var loadUrl = "ajax/load.php";
		//var loadUrl = "http://127.0.0.1:8000/inventario/";
		var loadUrl = "http://127.0.0.1:8000/inventario/json_test.json/";
		$("#result").html(ajax_load).load(loadUrl);
		    
		return false;
	});
		
	function perform_item_selection(item_id) {
		//When invoked will verify if any of reorder or exist boxes
		//are checked, to enable/disable the matching (hidden) items collection
		var chk_reorder = $("#form_canvas #entry_frame_" + item_id + " #isreorder_" + item_id);
		var chk_exist   = $("#form_canvas #entry_frame_" + item_id + " #isexist_" + item_id);
		var chk_item    = $("#form_canvas #entry_frame_" + item_id + " .item");
		var to_check    = chk_reorder.is(':checked') || chk_exist.is(':checked');
		
		if(to_check) {
			chk_item.attr("checked", "checked");
		} else {
			chk_item.removeAttr("checked");
		}
	}
	
	$("form#inventory input[name^=qty]").change(function() {
		//change on quantity text field checks checkbox
		var id = $(this).attr('id');
		var suffix = "exist";
				
		if (id.indexOf("reorder") > -1) {
			suffix = "reorder";
		}
			
		var item_id = id.split("qty_" + suffix + "_")[1];
		
		if( $(this).val().trim() ) {
			var chkbox  = $("#form_canvas #entry_frame_" + item_id + " #is" + suffix + "_" + item_id); //Example: $("#form_canvas #entry_frame_1  #isreorder_1")
			chkbox.attr("checked", "checked");
						
			var item = $("#form_canvas .cell #" + item_id);
			item.attr("checked", "checked");
		} else {
			//Do nothing, current implementation means
			//the user wants the item in the inventory but 
			//don't want to add a quantity
		}
		
		perform_item_selection(item_id);
	});
	
	$("form#inventory input[name^=is]").change(function() {
		//change on exist or reorder checkbox
		var id = $(this).attr('id');
		var suffix = "exist";
				
		if (id.indexOf("reorder") > -1) {
			suffix = "reorder";
		}
		var item_id 	= id.split("is" + suffix + "_")[1];
		perform_item_selection(item_id);
	});
	
	$("form#inventory span[id^=entry_canvas_]").click(function() {
		//click on item caption toggles item checkbox

		var id = $(this).attr('id');
		var item_id = id.split("entry_canvas_")[1];
				
		chkbox =  $("#entry_frame_" + item_id + " #isexist_" + item_id); //Example: "#entry_frame_2 #2"
		
		if(chkbox.attr('checked')) { //if(chkbox.is(':checked')) {		
			chkbox.removeAttr("checked");
		} else {
			chkbox.attr("checked", "checked");
		}
	});
	
	$("input#date").click(function() {
		var dd    = new Date();
        var day   = dd.getDate();
        var month = dd.getMonth();
        var year  = dd.getFullYear();
        var todayDate = day + "/" + month + "/" + year;
		$("form#inventory input#id_name").val(todayDate);
		return false;
	});	
	
	$("input#last").click(function() {
		return false;
	});
	
	$("form#inventory_view #units").click(function() {
		$(".row .unit").toggle()
		return false;
	});
	$("form#inventory_view #qty").click(function() {
		$(".row .qty").toggle()
		return false;
	});
	
	$("input[name='ttype']").change(function() {
		$("#form_canvas .optional").toggle();
	});
});
