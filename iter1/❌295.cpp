// 两个heap，保证各放一半的元素

class MedianFinder {
	priority_queue<long> small, large;
	
public:
	/** initialize your data structure here. */
	MedianFinder() {
		
	}
	
	void addNum(int num) {
		small.push(num);
		large.push(-small.top());
		small.pop();
		if (large.size() >= small.size()) {
			small.push(-large.top());
			large.pop();
		}
	}
	
	double findMedian() {
		if (small.size() == large.size()) return (small.top() + large.top()) / 2.0;
		else return small.top();
	}
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */