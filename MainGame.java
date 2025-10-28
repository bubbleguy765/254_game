import java.util.*;

class Card {
    private int value;

    public Card(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }
}

class Deck {
    private ArrayList<Card> deck = new ArrayList<>();

    public Deck() {
        reset();
    }

    public void reset() {
        deck.clear();
        int[] cardValues = {11, 10, 9, 8, 7, 6, 5, 4, 3, 2};

        for (int i = 0; i < cardValues.length; i++) {
            int value = cardValues[i];
            int count;
            if (value == 10) {
                count = 16;
            } else {
                count = 4;
            }
            for (int j = 0; j < count; j++) {
                deck.add(new Card(value));
            }
        }
    }

    public void shuffle() {
        Collections.shuffle(deck);
    }

    public Card deal() {
        if (!deck.isEmpty()) {
            return deck.remove(deck.size() - 1);
        } else {
            return null;
        }
    }
}

class Hand {
    private ArrayList<Card> cards = new ArrayList<>();
    private int value = 0;
    private int aces = 0;

    public void addCard(Card c) {
        cards.add(c);
        value = value + c.getValue();
        if (c.getValue() == 11) {
            aces = aces + 1;
        }
    }

    public int getValue() {
        int total = value;
        int tempAces = aces;
        while (total > 21 && tempAces > 0) {
            total = total - 10;
            tempAces = tempAces - 1;
        }
        return total;
    }
}

public class MainGame {
    private Deck deck;
    private Hand player;
    private Hand dealer;
    private String playerName;
    private Scanner input;

    public MainGame(String name) {
        playerName = name;
        input = new Scanner(System.in);
        deck = new Deck();
        deck.shuffle();
        player = new Hand();
        dealer = new Hand();
    }

    public void playRound() {
        for (int i = 0; i < 2; i = i + 1) {
            player.addCard(deck.deal());
            dealer.addCard(deck.deal());
        }
        while (true) {
            if (player.getValue() > 21) {
                System.out.println("You busted.");
                return;
            }

            System.out.print("h to hit or s to stand: ");
            String choice = input.nextLine();

            if (choice.equals("h")) {
                Card newCard = deck.deal();
                player.addCard(newCard);
            } else if (choice.equals("s")) {
                continue;
            }
        }
        while (dealer.getValue() < 17) {
            dealer.addCard(deck.deal());
        }

        int playerTotal = player.getValue();
        int dealerTotal = dealer.getValue();

        System.out.println(playerName + " value: " + playerTotal);
        System.out.println("D value " + dealerTotal);

        if (dealerTotal > 21) {
            System.out.println("Dealer busted; ");
        } else if (playerTotal > dealerTotal) {
            System.out.println("You win! ");
        } else if (playerTotal < dealerTotal) {
            System.out.println("Dealer wins.");
        } else {
            System.out.println("Tie.");
        }
    }
}
