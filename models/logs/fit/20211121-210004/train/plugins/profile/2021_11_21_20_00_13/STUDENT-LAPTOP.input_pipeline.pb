	b??4???@b??4???@!b??4???@	??l???d???l???d?!??l???d?"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$b??4???@?z?G???As?r??@YI??&??*	ffffffX@2F
Iterator::ModelǺ?????!\2?h?F@)	?c???1?6?S\?:@:Preprocessing2v
?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[2]::TensorSlice??_?L??!?:ڼO5@)??_?L??1?:ڼO5@:Preprocessing2U
Iterator::Model::ParallelMapV2?l??????!*.?u?2@)?l??????1*.?u?2@:Preprocessing2l
5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat;?O??n??!?:ڼOq2@)2??%䃎?1lާ?d?.@:Preprocessing2f
/Iterator::Model::ParallelMapV2::Zip[0]::FlatMap?:pΈҞ?!?????>@)Έ?????1??%C?#@:Preprocessing2Z
#Iterator::Model::ParallelMapV2::ZipF%u???!????K@)U???N@s?1i?>?%C@:Preprocessing2x
AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensora??+ei?!T\2?h	@)a??+ei?1T\2?h	@:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
device?Your program is NOT input-bound because only 0.0% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*no9??l???d?I&?????X@Zno#You may skip the rest of this page.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	?z?G????z?G???!?z?G???      ??!       "      ??!       *      ??!       2	s?r??@s?r??@!s?r??@:      ??!       B      ??!       J	I??&??I??&??!I??&??R      ??!       Z	I??&??I??&??!I??&??b      ??!       JCPU_ONLYY??l???d?b q&?????X@