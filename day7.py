with open('inputs/day7_input.txt') as f:
    s = f.read().replace('bags', 'bag').strip()

rules = s.split('.\n')

def get_outer_bags(rules, tracked_bags, bag_to_find):
    for rule in rules:
        if ' ' + bag_to_find in rule:
            next_outer_bag = rule.split(' bag contain')[0]
            if next_outer_bag in tracked_bags:
                continue
            tracked_bags.add(next_outer_bag)
            tracked_bags = tracked_bags | get_outer_bags(rules, tracked_bags, next_outer_bag)
    return tracked_bags

tracked_outer_bags = set()
tracked_outer_bags = get_outer_bags(rules, tracked_outer_bags, 'shiny gold')
print(len(tracked_outer_bags))

def get_inner_bags(rules, current_bag):
    for rule in rules:
        if current_bag + ' bag contain' not in rule:
            continue
        inner_bags = ' '.join(rule.split('bag contain ')[1:]) + ', '
        if 'no other bag' in inner_bags:
            return 1
        return 1 + sum([int(bag.split()[0]) * get_inner_bags(rules, ' '.join(bag.split()[1:])) for bag in inner_bags.split(' bag, ') if bag])

print(get_inner_bags(rules, 'shiny gold')-1)
