class Solution {
public:
    void merge(vector<int>& arr, int low, int mid, int high){
        int i = low;
        int j = mid + 1;
        int k = low;
        int temp[high + 1];
        while(i <= mid && j <= high){
            if(arr[i] < arr[j]){
                temp[k++] = arr[i++];
            }
            else{
                temp[k++] = arr[j++];
            }
        }
        while(i <= mid){
            temp[k++] = arr[i++];
        }
        while(j <= high){
            temp[k++] = arr[j++];
        }
        for(int x = low; x <= high; x++){
            arr[x] = temp[x];
        }
    }
    
    void mergeSort(vector<int>& arr, int low, int high){
        if(low >= high) return;
        int mid = low + (high - low) / 2;
        mergeSort(arr, low, mid);
        mergeSort(arr, mid + 1, high);
        merge(arr, low, mid, high);
    }
    
    vector<int> sortArray(vector<int>& arr) {
        int n = arr.size();
        mergeSort(arr, 0, n - 1);
        return arr;
    }
};