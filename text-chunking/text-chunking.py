def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # 1. Compute the step size between chunk start positions
    step = chunk_size - overlap
    chunks = []
    
    # 2. Starting from position 0
    current_start = 0
    
    # 3. Process tokens until a chunk reaches the end of the list
    # The constraints guarantee tokens has at least 1 element, so the loop runs at least once.
    while current_start < len(tokens):
        # Extract a chunk of up to chunk_size tokens
        chunk = tokens[current_start : current_start + chunk_size]
        chunks.append(chunk)
        
        # 4. Check if this chunk reached the end of the token list
        # If the end index of the slice is >= length of tokens, we are done.
        if current_start + chunk_size >= len(tokens):
            break
            
        # 5. Advance the starting position by the calculated step
        current_start += step
        
    return chunks