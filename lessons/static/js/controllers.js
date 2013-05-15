'use strict';

/* Controllers */

//Controler ExerciseListCtrl
//Retrieves the model Exercises

function SolutionCtrl($scope,$http){
    $scope.url = '/polingua/words/ajax/validate/'; // The url of our search
         
    // The function that will be executed on button click (ng-click="search()")
    $scope.validate = function() {
         
        // Create the http post request
        // the data holds the keywords
        // The request is a JSON request.
        $http.post($scope.url, { "data" : $scope.solution}).
        success(function(data, status) {
            $scope.status = status;
            $scope.data = data;
            $scope.result = data; // Show result from server in our <pre></pre> element
        })
        .
        error(function(data, status) {
            $scope.data = data || "Request failed";
            $scope.status = status;         
        });
    };
}


function ExerciseCtrl($scope,$http) {
	$http.get('/api/v1/exercise?format=json').success(
		function(data){
			$scope.exercise = data['objects'][0]
			console.log($scope.exercise)
		})
		.error(function(data){
			console.log('error')
		});
}

function ExerciseListCtrl($scope,$http) {
	$http.get('/api/v1/exercise?format=json').success(
		function(data) {
			$scope.exercises = data['objects'];
	})
	.error(function(data){
		console.log('error')
	});
	
}

angular.module('mainapp', [])
    .factory('mathem', function () {
        return {
            div: function (arg1,arg2) {
                return arg1/arg2;
            }
        }
    });
        
function MyController($scope, mathem){
    $scope.div = mathem.div;
}