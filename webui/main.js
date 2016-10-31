angular.module('lightApp', ['ngMaterial', 'ngMdIcons', 'ngCookies'])
         
.controller("lightController", function($scope, $http, $q, $mdDialog, $cookies, $mdToast) {
    $scope.pickerColor = {red: 255, green: 64, blue: 129}
    $scope.color = $scope.pickerColor
    $scope.mono = 50
    $scope.baseUrl = ($cookies.baseUrl!=null) ? $cookies.baseUrl : "http://localhost:8001"
    $scope.delay = 60
    $scope.notLoading = false

    $http.get($scope.baseUrl+'/getZoneInfo/').then(
        function successCallback(response){
            $scope.zones = []
            for(var zone in response.data){
                $scope.zones.push({name: 'Zone '+(parseInt(zone)+1), zoneNumber: parseInt(zone), description: response.data[zone].description, type: response.data[zone].type.  toUpperCase()})
          }
          $scope.currentZone = $scope.zones[0]
          $scope.testMode = false
          $scope.notLoading = true
        },
        function errorCallback(response){
          $scope.zones = [
            {name: 'Zone 1', zoneNumber: 0, description: 'The first zone', type: 'RGB'},
            {name: 'Zone 2', zoneNumber: 1, description: 'The second zone', type: 'MONO'} 
          ]
          $scope.currentZone = $scope.zones[0]
          $scope.testMode = true
          $scope.notLoading = true
        }
    )

    $scope.showPrerenderedDialog = function(ev) {
    $mdDialog.show({
      controller: DialogController,
      contentElement: '#myDialog',
      parent: angular.element(document.body),
      targetEvent: ev,
      clickOutsideToClose: true
    });
  };

  $scope.offButton = function(){
    request = $scope.baseUrl+'/setLights/'
    if($scope.currentZone.type == 'RGB'){
      params = {red: 0, green: 0, blue: 0, zone: $scope.currentZone.zoneNumber}
      $http.get(request, {
        params: params
      }).then(
        function successCallback(response){
          $mdToast.show($mdToast.simple().textContent('Lights Off'));
        }
      )
    }
    else{
      params = {mono: 0, zone: $scope.currentZone.zoneNumber}
      $http.get(request, {
        params: params
      }).then(
        function successCallback(response){
          $mdToast.show($mdToast.simple().textContent('Lights Off'));
        }
      )
    }
  }

  $scope.saveBaseUrl = function(){
    $cookies.baseUrl = $scope.baseUrl
    $mdToast.show($mdToast.simple().textContent('Settings Updated - Refresh page to reload zones'));
    $mdDialog.hide()
  }

  $scope.showPrerenderedScheduleDialog = function(ev) {
    $mdDialog.show({
      controller: DialogController,
      contentElement: '#scheduleDialog',
      parent: angular.element(document.body),
      targetEvent: ev,
      clickOutsideToClose: true
    });
  };

  $scope.setColorFromPicker = function(color) {
    $scope.color = {red: color[0], green: color[1], blue: color[2]}
    $scope.pickerColor = $scope.color
  }

  $scope.setMonoFromPicker = function(mono){
    $scope.mono = mono
  }

  $scope.colors = [
    [255,0,0],
    [0,255,0],
    [0,0,255],
    [255,255,0],
    [0,255,255],
    [255,0,255]
  ]

  $scope.rgbIntensities = [
    [63,63,63,'25'],
    [127,127,127,'50'],
    [191,191,191,'75'],
    [255,255,255,'100']
  ]

  $scope.monoIntensities = [
    [25,'25'],
    [50,'50'],
    [75,'75'],
    [100,'100']
  ]

  $scope.demo = {
        isOpen: false,
        count: 0,
        selectedDirection: 'left'
      };

  $scope.mq = window.matchMedia( "(min-width: 600px)" ).matches;

  $scope.scheduleLights = function(){
    $scope.setLights(true)

  }
  $scope.delayDialog = false
  $scope.setLights = function(delay=false){
    request = (delay) ? $scope.baseUrl+'/setEvent/' : $scope.baseUrl+'/setLights/'
    if($scope.currentZone.type == 'RGB'){
      params = {red: $scope.pickerColor.red, green: $scope.pickerColor.green, blue: $scope.pickerColor.blue, zone: $scope.currentZone.zoneNumber}
      if(delay != false){
        params.delay = Math.floor($scope.delay*60)
      }
      $http.get(request, {
        params: params
      }).then(
        function successCallback(response){
          $mdToast.show($mdToast.simple().textContent((delay) ? 'Lights Scheduled' : 'Lights Set'));
        }
      )
    }
    else{
      params = {mono: Math.floor($scope.mono*2.55), zone: $scope.currentZone.zoneNumber}
      if(delay != false){
        params.delay = Math.floor($scope.delay*60)
      }
      $http.get(request, {
        params: params
      }).then(
        function successCallback(response){
          $mdToast.show($mdToast.simple().textContent((delay) ? 'Lights Scheduled' : 'Lights Set'));
        }
      )
    }
    if(delay){
      $mdDialog.hide()
    }
  }

  $scope.updateZone = function(zone) {
    $scope.currentZone = zone;
  }
  function DialogController($scope, $mdDialog) {
    $scope.hide = function() {
      $mdDialog.hide();
    };

    $scope.cancel = function() {
      $mdDialog.cancel();
    };

    $scope.answer = function(answer) {
      $mdDialog.hide(answer);
    };
  }
});
