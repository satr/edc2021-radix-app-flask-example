# radix-app-custom-metrics-flask

Horizontal pod autoscaling changes number of replicas (pods) of the component, within a specified min-max range:
* when CPU load is low - number of replicas are minimum
* when CPU load grows up - new replicas started, up to specified max number
* when CPU load drops to low - number of replicas drops (within few minutes) , down to specified min number

Define property horizontalScaling in radixconfig.yaml for component environment config with min-max values
```
  horizontalScaling:
    minReplicas: 2
    maxReplicas: 6
```
