const BASE_URL = "/api/cupcakes";
$cupcakeList = $("#cupcake-list");

/* GET request to display all the cupcakes */
async function fetchCupcakeList(){
  const response = await axios.get(BASE_URL);
  let cupcakeList = response.data.cupcakes;

  console.log(response.data.cupcakes)

  for(let cupcake of cupcakeList){
    generateMarkupAndAppend(cupcake);
  }
}

/* Genereate markup for each cupcake and append it to index.html */
function generateMarkupAndAppend(cupcake){
  let html = `<img class="img-thumbnail w-25" src="${cupcake.image}">
              <li>${cupcake.flavor}, ${cupcake.size}, 
              ${cupcake.rating}</li>`;

  $cupcakeList.append(html);
}


/* After page loads, fetch the cupcakes list */
// $( document ).ready(function(){
//   fetchCupcakeList();
// });


fetchCupcakeList();
