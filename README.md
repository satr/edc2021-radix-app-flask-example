# radix-app-custom-metrics-flask

* Each component of a Radix application gets default amount of CPU and memory resources
* Resources can be customized entirely or partially individually for component of its environment

Define property resources in `radixconfig.yaml` for component of its environment
```yaml
      resources:
        requests:
          memory: "50Mi"
          cpu: "50m"
        limits:
          memory: "200Mi"
          cpu: "200m"  
```