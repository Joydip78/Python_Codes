from collections import Counter

def max_difference(s: str, k: int) -> int:
    n = len(s)
    max_diff = float('-inf')
    
    for window_size in range(k, n + 1):
        freq = Counter(s[:window_size])
        
        # process initial window
        odd_chars = [c for c in freq if freq[c] % 2 == 1]
        even_chars = [c for c in freq if freq[c] % 2 == 0]
        
        for a in odd_chars:
            for b in even_chars:
                max_diff = max(max_diff, freq[a] - freq[b])
        
        # Slide window
        for i in range(1, n - window_size + 1):
            out_char = s[i - 1]
            in_char = s[i + window_size - 1]
            
            freq[out_char] -= 1
            if freq[out_char] == 0:
                del freq[out_char]
            freq[in_char] += 1
            
            odd_chars = [c for c in freq if freq[c] % 2 == 1]
            even_chars = [c for c in freq if freq[c] % 2 == 0]
            
            for a in odd_chars:
                for b in even_chars:
                    max_diff = max(max_diff, freq[a] - freq[b])
    
    return max_diff if max_diff != float('-inf') else -1

x = max_difference("331200430414242010434303011200032333",
1)
print(x)