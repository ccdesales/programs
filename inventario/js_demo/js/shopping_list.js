$(document).ready(function() {
	
	//Function that receives and element id ans splits it
	//in components: category id and item id, 
	//which are separated by an underscore (_)
	function get_item_ids(id) {
		var arr = id.split("_");
		return [arr[0], arr[1]];
	};

	$(".item").click(function() {
		var id = $(this).attr('id');
		var ids = get_item_ids(id);
		
		var category_id = ids[0];
		var item_id 	= ids[1];
				
		//element and right_element required to decide if the
		//clicked item is going to be moved right or left
		var elem_expression = ".category #" + id + ".item"
		var element  = $("#left " + elem_expression);
		var right_element = $("#right " + elem_expression);
		
		var new_parent = $("#right #R" + category_id + ".category");
		
		//item by default located in the left pane
		//decide if it is instead on the right
		if (right_element.length > 0) {
			element = right_element;
			new_parent = $("#left #L" + category_id + ".category");
		} 
		
		//Perform actual move
		element.detach().appendTo(new_parent);
 	});
});
