from abc import ABC, abstractmethod
import business_layer

class SystemService(ABC):

    @abstractmethod
    def enter_landing_page_url(self, url):
        """
        purpose: receives a landing page url.
        :param url: landing page url
        :return: void
        """
        pass

    @abstractmethod
    def scan_landing_page(self, url):
        """
        purpose: scan a landing page url.
        :param url: landing page url
        :return: void
        """
        pass

    @abstractmethod
    def extract_keywords_from_landing_page(self, url):
        """
        purpose: extract keywords from  a landing page.
        :param url: landing page url
        :return: list of keywords
        """
        pass

    @abstractmethod
    def add_scraping_rule(self, new_rule):
        """
        purpose: add a new rule for scraping a landing page
        :param new_rule:
        :return: void
        """
        pass

    @abstractmethod
    def edit_a_scraping_rule(self, rule_id):
        """
        purpose: edit an existing scraping rule.
        :param rule_id:
        :return: void
        """
        pass

    @abstractmethod
    def connect_to_image_repositories(self, image_repos):
        """
        purpose: connects to the specified image repositories.
        :param image_repos: a list of image repositories API's to connect
        :return: void
        """
        pass

    @abstractmethod
    def disconnect_from_image_repositories(self, image_repos):
        """
        purpose: disconnects from the specified image repositories.
        :param image_repos: a list of image repositories API's to disconnect from
        :return: void
        """
        pass

    @abstractmethod
    def recommend_n_photos_by_keywords(self, image_repos, keywords, n):
        """
        purpose: returns the most n relevant photos for the given keywords, from image_repos
         repositories.
        :param n: number of photos to be recommended
        :param keywords: keywords for choosing the photos
        :param image_repos: a list of image repositories API's to search from
        :return: n most relevant photos
        """
        pass

    @abstractmethod
    def recommend_n_photos_by_landing_page(self, image_repos, landing_url, n):
        """
        purpose: scrape the landing page given in landing_url. Returns the most n relevant photos
        from image_repos, given the landing page.
         repositories.
        :param landing_url: url of a landing page
        :param n: number of photos to be recommended
        :param image_repos: a list of image repositories API's to search from
        :return: n most relevant photos
        """
        pass

    @abstractmethod
    def process_image_from_a_repository(self, image):
        """
        purpose: receives an image, processes it and returns the image's metadata.
        :param image: image to be processes
        :return: metadata extracted from the image
        """
        pass

    @abstractmethod
    def get_error_log(self):
        """
        purpose: returns error log
        :return: error log
        """
        pass

    @abstractmethod
    def get_action_log(self):
        """
        purpose: returns action log
        :return: action log
        """
        pass
