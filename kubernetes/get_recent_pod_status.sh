cd ~/w4
bazel run //cabinet/iris/experimental/jaeseungbyun:csv_show
sleep 15
pod_name=`kubectl get pods --sort-by=.metadata.creationTimestamp -o jsonpath="{.items[-1].metadata.name}"`
echo $pod_name
status=`kubectl get pods $pod_name | grep Completed`
echo $status

if [ "$status" == '' ];
then
	echo "status error"
else
	echo "status completed"
fi
