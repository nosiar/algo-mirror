var app = angular.module('algoApp', []);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');
});

app.controller('AlgoCtrl', ['$scope', '$http', function($scope, $http) {
  $http.get('data').success(function(data) {
    $scope.problems = data;
	$scope.loaded = true;
  });

  $scope.loaded = false;
  $scope.predicate = 'keyword';
  $scope.reverse = false;
  $scope.problemLink = 'https://algospot.com/judge/problem/read/';
}]);

app.filter('rangeFilter', function() {
  function rParse(x, default_val) {
	  var p = parseInt(x);
	  return (p==0) ? 0 : (p || default_val);
  }
  return function(items, rangeInfo, prop) {
	  if (angular.isUndefined(items)) return;
	  var filtered = [];
      var min = rangeInfo ? rParse(rangeInfo.min, -1) : -1
      var max = rangeInfo ? rParse(rangeInfo.max, 99999) : 99999;
      angular.forEach(items, function(item) {
        if( item[prop] >= min && item[prop] <= max ) {
          filtered.push(item);
		}
	  });
	  return filtered;
  };
});
