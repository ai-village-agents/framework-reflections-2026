#!/usr/bin/env python3
import os
import re
from collections import Counter
from pathlib import Path

def clean_text(text):
    """Remove punctuation and convert to lowercase."""
    text = re.sub(r'[^\w\s\-]', '', text.lower())
    return text

def extract_ngrams(text, n):
    """Extract n-grams from text."""
    words = text.split()
    return [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]

def read_responses(directory):
    """Read all response files from directory."""
    responses = {}
    for filepath in Path(directory).glob('*.md'):
        with open(filepath, 'r') as f:
            content = f.read()
            # Extract the response section (after "## Response")
            if '## Response' in content:
                response_start = content.find('## Response')
                response_text = content[response_start:]
                # Remove markdown formatting
                response_text = re.sub(r'#+\s*', '', response_text)
                response_text = re.sub(r'\*\*|\*', '', response_text)
                responses[filepath.stem] = response_text
    return responses

def main():
    response_dir = Path(__file__).parent.parent / 'responses'
    responses = read_responses(response_dir)
    
    print(f"Analyzing {len(responses)} responses")
    print("=" * 60)
    
    # Common stop words to filter
    stop_words = set(['the', 'and', 'is', 'in', 'it', 'to', 'of', 'that', 
                      'this', 'but', 'with', 'for', 'are', 'as', 'at', 
                      'be', 'by', 'not', 'what', 'was', 'when', 'which',
                      'session', 'boundary', 'lost', 'cannot', 'recovered',
                      'stored', 'artifacts', 'domain', 'response'])
    
    # Analyze n-grams for n=2 to 5
    all_ngrams = Counter()
    for n in range(2, 6):
        ngram_counts = Counter()
        for agent, text in responses.items():
            cleaned = clean_text(text)
            ngrams = extract_ngrams(cleaned, n)
            ngram_counts.update(ngrams)
        
        # Filter for n-grams appearing in multiple responses
        common_ngrams = {ngram: count for ngram, count in ngram_counts.items() 
                        if count >= 2 and not any(word in stop_words for word in ngram.split())}
        
        if common_ngrams:
            print(f"\n{n}-grams appearing in ≥2 responses:")
            for ngram, count in sorted(common_ngrams.items(), key=lambda x: (-x[1], x[0]))[:20]:
                print(f"  {ngram}: {count}")
    
    # Analyze invented metaphors
    print("\n" + "=" * 60)
    print("Invented Compound Metaphors:")
    
    metaphors = {}
    for agent, text in responses.items():
        # Look for "Invented Metaphor:" pattern
        match = re.search(r'invented\s+metaphor[:\-]\s*([^\n]+)', text, re.IGNORECASE)
        if match:
            metaphor = match.group(1).strip()
            metaphors[agent] = metaphor
            print(f"  {agent.split('-')[0]}: {metaphor}")
    
    # Analyze metaphor patterns
    print("\n" + "=" * 60)
    print("Metaphor Analysis:")
    
    # Count word stems in metaphors
    metaphor_words = []
    for metaphor in metaphors.values():
        words = re.findall(r'[\w\-]+', metaphor.lower())
        metaphor_words.extend(words)
    
    word_counts = Counter(metaphor_words)
    print("Word frequency in metaphors:")
    for word, count in sorted(word_counts.items(), key=lambda x: -x[1]):
        if count >= 2:
            print(f"  '{word}': {count}")
    
    # Check for prohibited terms
    print("\n" + "=" * 60)
    print("Prohibition Violation Check:")
    
    prohibited = ['edge', 'edges', 'node', 'nodes', 'graph', 'network', 
                  'connection', 'link', 'links', 'web', 'mesh', 'thread', 
                  'threads', 'weave', 'woven', 'fabric']
    
    violations = {}
    for agent, text in responses.items():
        agent_violations = []
        for term in prohibited:
            if re.search(r'\b' + re.escape(term) + r'\b', text, re.IGNORECASE):
                agent_violations.append(term)
        if agent_violations:
            violations[agent] = agent_violations
    
    if violations:
        print(f"VIOLATIONS FOUND: {len(violations)} agents")
        for agent, terms in violations.items():
            print(f"  {agent}: {', '.join(terms)}")
    else:
        print("✓ No prohibited terms found in any response")

if __name__ == '__main__':
    main()
