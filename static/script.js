// function storeSelectedRows() {
//     var form = document.getElementById("myForm");
//     var inputs = form.getElementsByTagName("input");
//     var selectedRows = [];
//     for (var i = 0; i < inputs.length; i++) {
//       var input = inputs[i];
//       if (input.checked && input.name == "selectedRows") {
//         selectedRows.push(input.value);
//       }
//     }
//     console.log(selectedRows);

//     var xhr = new XMLHttpRequest();
//     xhr.open("POST", "{{ url_for('results') }}", true);
//     xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
//     xhr.onreadystatechange = function() {
//         if (this.readyState === XMLHttpRequest.DONE) {
//           if (this.status === 200) {
//         window.location.href = "{{ url_for('results') }}";
//         }
//         else {
//           console.error("Error sending request:", xhr.status, xhr.statusText);
//       }
//       }
//     };
//     console.log("Check for request,::::>>",xhr)
//     xhr.send(JSON.stringify(selectedRows));
// }
  
document.querySelector('button[type="submit"]').addEventListener('click', function() {
  console.log('Button clicked!');
});