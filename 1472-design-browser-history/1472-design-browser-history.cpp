class DoublyLinkedListNode{
public:
    string data;
    DoublyLinkedListNode *prev, *next;
    DoublyLinkedListNode(string url){
        data = url;
        prev = NULL;
        next = NULL;
    }
};

class BrowserHistory {
public:
    DoublyLinkedListNode* head;
    DoublyLinkedListNode* current;
    
    BrowserHistory(string homepage) {
        head = new DoublyLinkedListNode(homepage);
        current = head;
    }
    
    void visit(string url) {
        DoublyLinkedListNode* newNode = new DoublyLinkedListNode(url);
        current->next = newNode;
        newNode->prev = current;
        current = newNode;
    }
    
    string back(int steps) {
        while(steps>0 && current->prev != NULL){
            current = current->prev;
            steps--;
        }
        return current->data;
    }
    
    string forward(int steps) {
        while(steps>0 && current->next != NULL){
            current = current->next;
            steps--;
        }
        return current->data;
    }
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */