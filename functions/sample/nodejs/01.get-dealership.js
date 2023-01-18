/**
  *
  * main() will be run when you invoke this action
  *
  * @param Cloud Functions actions accept a single parameter, which must be a JSON object.
  *
  * @return The output of this action, which must be a JSON object.
  *
  */
const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');

function main(params) {

    const authenticator = new IamAuthenticator({ apikey: params.IAM_API_KEY })
    const cloudant = CloudantV1.newInstance({
      authenticator: authenticator
    });
    cloudant.setServiceUrl(params.COUCH_URL);

    return getAllRecords(cloudant, "dealerships");
}

 /*
 Sample implementation to get all the records in a db.
 */
 function getAllRecords(cloudant,dbname) {
     return new Promise((resolve, reject) => {
         cloudant.postAllDocs({ db: dbname, includeDocs: true, limit: 10 })            
             .then((result)=>{
              console.log(result.result.rows)
              resolve({ result: result.result.rows });
             })
             .catch(err => {
                console.log(err);
                reject({ err: err });
             });
         })
 }
/*
{
    "IAM_API_KEY": "vIu9HaKiRhjDxioRa24NhIKdxETRuWRJDhP8_fU9FWfc",
    "COUCH_URL": "https://b65d1bed-d060-4cb3-91b4-ba3cbb0b7e16-bluemix.cloudantnosqldb.appdomain.cloud"
}
*/