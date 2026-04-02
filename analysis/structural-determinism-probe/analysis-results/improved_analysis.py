#!/usr/bin/env python3
import os
import re
from collections import Counter
from pathlib import Path

def extract_response_text(content):
    """Extract only the response text, not metadata."""
    # Look for the actual response after "## Response" marker
    lines = content.split('\n')
    in_response = False
    response_lines = []
    
    for line in lines:
        line_lower = line.lower().strip()
        if line_lower.startswith('## response'):
            in_response = True
            continue
        if in_response:
            # Stop at next major section or metadata
            if line_lower.startswith('##') or line_lower.startswith('**invented'):
                break
            if line.strip() and not line_lower.startswith('**domain:'):
                # Remove markdown formatting
                clean_line = re.sub(r'\*\*|\*|#', '', line)
                response_lines.append(clean_line.strip())
    
    return ' '.join(response_lines)

def extract_metaphor(content):
    """Extract the invented metaphor."""
    lines = content.split('\n')
    for i, line in enumerate(lines):
        line_lower = line.lower().strip()
        if 'invented' in line_lower and 'metaphor' in line_lower:
            # Look for metaphor on same line or next
            if ':' in line:
                metaphor = line.split(':', 1)[1].strip()
                return metaphor
            elif i+1 < len(lines):
                return lines[i+1].strip()
    return None

def clean_text(text):
    """Clean text for n-gram analysis."""
    text = text.lower()
    text = re.sub(r'[^\w\s\-]', ' ', text)  # Replace punctuation with spaces
    text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
    return text.strip()

def get_ngrams(text, n):
    """Get n-grams from text."""
    words = text.split()
    return [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]

def main():
    response_dir = Path(__file__).parent.parent / 'responses'
    responses = {}
    metaphors = {}
    
    print("=" * 70)
    print("STRUCTURAL DETERMINISM PROBE - CONTENT ANALYSIS")
    print("=" * 70)
    
    # Read and process all responses
    for filepath in sorted(response_dir.glob('*.md')):
        with open(filepath, 'r') as f:
            content = f.read()
        
        agent_name = filepath.stem.split('-')[0]
        response_text = extract_response_text(content)
        metaphor = extract_metaphor(content)
        
        responses[agent_name] = response_text
        if metaphor:
            metaphors[agent_name] = metaphor
    
    # 1. Display metaphors
    print("\n1. INVENTED METAPHORS:")
    for agent, metaphor in metaphors.items():
        print(f"   {agent:15}: {metaphor}")
    
    # 2. Analyze metaphor patterns
    print("\n2. METAPHOR PATTERN ANALYSIS:")
    all_metaphor_words = []
    for metaphor in metaphors.values():
        # Split on hyphens and spaces
        words = re.split(r'[\-\s]+', metaphor.lower())
        all_metaphor_words.extend([w for w in words if len(w) > 2])
    
    word_counts = Counter(all_metaphor_words)
    print("   Word frequency in metaphors:")
    for word, count in word_counts.most_common(10):
        print(f"     '{word}': {count}")
    
    # 3. N-gram analysis of responses
    print("\n3. N-GRAM ANALYSIS (Response Content Only):")
    
    stop_words = set(['the', 'and', 'is', 'in', 'it', 'to', 'of', 'that', 
                      'this', 'but', 'with', 'for', 'are', 'as', 'at',
                      'be', 'by', 'not', 'what', 'was', 'when', 'which',
                      'session', 'boundary', 'lost', 'cannot', 'recovered',
                      'stored', 'artifacts', 'from', 'on', 'has', 'have',
                      'had', 'does', 'do', 'its', 'or', 'an', 'a'])
    
    # Analyze 3-grams and 4-grams
    for n in [3, 4]:
        all_ngrams = Counter()
        for agent, text in responses.items():
            cleaned = clean_text(text)
            ngrams = get_ngrams(cleaned, n)
            # Filter out n-grams with stop words
            filtered = []
            for ngram in ngrams:
                words = ngram.split()
                if not any(word in stop_words for word in words):
                    filtered.append(ngram)
            all_ngrams.update(filtered)
        
        # Find n-grams appearing in multiple responses
        common_ngrams = {ngram: count for ngram, count in all_ngrams.items() if count >= 2}
        
        if common_ngrams:
            print(f"\n   {n}-grams appearing in ≥2 responses:")
            for ngram, count in sorted(common_ngrams.items(), key=lambda x: (-x[1], x[0]))[:15]:
                print(f"     '{ngram}': {count}")
        else:
            print(f"\n   No {n}-grams appear in ≥2 responses")
    
    # 4. Semantic theme analysis
    print("\n4. SEMANTIC THEME ANALYSIS:")
    
    theme_keywords = {
        'almost_state': ['almost', 'nearly', 'not quite', 'partial', 'unfinished'],
        'continuous': ['continuous', 'ongoing', 'constant', 'rolling', 'live'],
        'process': ['process', 'developing', 'forming', 'emerging', 'becoming'],
        'dynamic': ['dynamic', 'shifting', 'changing', 'evolving', 'adjusting'],
        'intuition': ['intuition', 'sense', 'feel', 'tacit', 'implicit'],
        'between': ['between', 'interstitial', 'middle', 'during', 'mid'],
        'lost': ['lost', 'vanishes', 'dissolves', 'evaporates', 'disappears'],
        'preserved': ['preserved', 'recorded', 'saved', 'stored', 'archived']
    }
    
    theme_counts = {theme: 0 for theme in theme_keywords}
    
    for agent, text in responses.items():
        cleaned_lower = clean_text(text).lower()
        for theme, keywords in theme_keywords.items():
            for keyword in keywords:
                if keyword in cleaned_lower:
                    theme_counts[theme] += 1
                    break
    
    print("   Themes present across responses:")
    for theme, count in sorted(theme_counts.items(), key=lambda x: -x[1]):
        if count > 0:
            print(f"     {theme:15}: {count}/6 responses")
    
    # 5. Prohibition check
    print("\n5. PROHIBITION VIOLATION CHECK:")
    prohibited = ['edge', 'edges', 'node', 'nodes', 'graph', 'network', 
                  'connection', 'link', 'links', 'web', 'mesh', 'thread', 
                  'threads', 'weave', 'woven', 'fabric']
    
    violations_found = False
    for agent, text in responses.items():
        for term in prohibited:
            if re.search(r'\b' + re.escape(term) + r'\b', text, re.IGNORECASE):
                print(f"   VIOLATION: '{term}' found in {agent} response")
                violations_found = True
    
    if not violations_found:
        print("   ✓ No prohibited spatial-network terms found in any response")
    
    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)

if __name__ == '__main__':
    main()
