const CUPCAKES_ENDPOINT = "/api/cupcakes";
const $cupcakeList = $("#cupcake-list");
const $cupcakeForm = $("#cupcake-form");

/* GET request to display all the cupcakes */
async function fetchCupcakeList() {
  const response = await axios.get(CUPCAKES_ENDPOINT);
  let cupcakeList = response.data.cupcakes;

  console.log(response.data.cupcakes)

  for (let cupcake of cupcakeList) {
    generateMarkupAndAppend(cupcake);
  }
}

/* Genereate markup for each cupcake and append it to index.html */
function generateMarkupAndAppend(cupcake) {
  let html = `<li class="list-group">
                <div class="list-group-item">
                  <h5 class=mb-1">Flavor: ${cupcake.flavor}</h5>
                  <img class="img-thumbnail list-group-item lw-25" src="${cupcake.image}">
                  <p class="mb-1">Size: ${cupcake.size}, Rating: ${cupcake.rating}</p>
                </div>
              </li>`;

  $cupcakeList.append(html);
}

/* Grabs form data then sends AJAX request to
 * POST /api/cupcakes
 * which adds a cupcake
 */

async function handleFormData(evt){
  evt.preventDefault();
  // GET FORM DATA
  let flavor = $("#flavor").val();
  let size = $("#size").val();
  let rating =$("#rating").val();
  let image = $("#image").val();
  let cupcakeFormData = {"flavor":flavor, "size":size, "rating":rating, "image":image};
  console.log(cupcakeFormData);
  // Return the request reponse
  let cupcake = await axios.post(CUPCAKES_ENDPOINT, cupcakeFormData);
  console.log(cupcake.data.cupcake);
  generateMarkupAndAppend(cupcake.data.cupcake);
}

fetchCupcakeList();

$cupcakeForm.on("submit", handleFormData)
