# radix-app-custom-metrics-flask


Example of metrics, returned by `/metrics` endpoint
```
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 972.0
python_gc_objects_collected_total{generation="1"} 108.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 90.0
python_gc_collections_total{generation="1"} 8.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="10",patchlevel="0",version="3.10.0"} 1.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 1.21479168e+08
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 3.6294656e+07
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.63541558451e+09
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 0.31999999999999995
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 6.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1.048576e+06
# HELP custom_request_count_total Request count
# TYPE custom_request_count_total counter
custom_request_count_total 3.0
# HELP custom_request_count_created Request count
# TYPE custom_request_count_created gauge
custom_request_count_created 1.6354155852482417e+09
# HELP custom_request_processing_seconds Time spent processing request
# TYPE custom_request_processing_seconds summary
custom_request_processing_seconds_count 3.0
custom_request_processing_seconds_sum 3.289099913672544e-05
# HELP custom_request_processing_seconds_created Time spent processing request
# TYPE custom_request_processing_seconds_created gauge
custom_request_processing_seconds_created 1.6354155852482636e+09
```