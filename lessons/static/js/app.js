angular.module('words', []).
  config(['$routeProvider', function($routeProvider) {
  $routeProvider.
      when('/exercise', {templateUrl: 'partials/exercise.html',   controller:ExerciseCtrl }).
      when('/exercises', {templateUrl: 'partials/exercises.html', controller:ExerciseListCtrl }).
      otherwise({redirectTo: '/'});
}]);